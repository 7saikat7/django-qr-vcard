import segno
from django.core.files import File
from django.core.files.storage import Storage
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


class VCard(models.Model):

    organization = models.CharField(
        _("Organization"),
        blank=False,
        max_length=150,
        default="",
    )
    name_first = models.CharField(
        _("First name"),
        blank=False,
        max_length=150,
        default="",
    )
    name_last = models.CharField(
        _("Last name"),
        blank=False,
        max_length=150,
        default="",
    )
    mobile_pers = models.CharField(
        _("Personal phone number"),
        blank=True,
        max_length=50,
        default="",
    )
    mobile_pro = models.CharField(
        _("Professional phone number"),
        blank=True,
        max_length=50,
        default="",
    )
    mail_pers = models.EmailField(
        _("Personal email"),
        blank=True,
        max_length=254,
        default="",
    )
    mail_pro = models.EmailField(
        _("Professional email"),
        blank=False,
        max_length=254,
        default="",
    )
    web_site = models.URLField(
        _("Web site"),
        blank=True,
        max_length=200,
        default="",
    )
    logo = models.ImageField(
        _("Logo"),
        upload_to='qr_vcard/logos/%y/%m/',
        blank=True,
        db_index=True,
        max_length=100,
        default="",
    )
    qrcode = models.ImageField(
        _("Qr code"),
        upload_to='qr_vcard/qrcodes/%Y/%m/',
        blank=True,
        null=True,
        db_index=True,
        max_length=100,
    )
    vcf = models.FileField(
        _("Vcard"),
        upload_to='qr_vcard/vcf_files/%Y/%m/',
        blank=True,
        null=True,
        db_index=True,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        obj = super().save(*args, **kwargs)
        vfile = obj.build_vcf()
        # do whatever you have with "vfile"

        # perform again save to save your fillings

        obj.save()
        return obj

    def get_full_name(self):
        """
        Gets the first name and the last name for data purposes
        (vcard file data).

        Returns:
            str: full name of a user
        """
        return f"{self.name_first} {self.name_last}"

    def get_file_name(self):
        """
        Gets the first name, the last name and
        the organization name for file naming purposes.

        Returns:
            str: name of vcf file
        """
        return f"{self.name_first}-{self.name_last}-{self.organization}"

    def build_vcf(self):
        """
        build_vcf is a method of :class:`VCard()` to store data
        of a user into a Vcard file (.vcf format):
        1) full name
        2) email (profesional and personal)
        3) telephone number (profesional and personal)
        4) name of organization
        5) website url
        6) link to logo

        Returns:
            File: a vcard file.
        """

        vcfLines = [
            'BEGIN:VCARD',
            'VERSION:4.0',
            f'FN:{self.get_full_name()}',
            f'EMAIL;TYPE=work:{self.mail_pro}',
            f'EMAIL;TYPE=home:{self.mail_pers}',
            f'TEL;TYPE=work:{self.mobile_pro}',
            f'TEL;TYPE=home:{self.mobile_pers}',
            f'ORG:{self.organization}',
            f'URL:{self.web_site}',
            # for LOGO, see if/else statement
            'END:VCARD',
            ]

        if self.logo.url is None:
            vcfLines.insert(9, 'LOGO:')
        else:
            vcfLines.insert(9, f'LOGO:{self.logo.url}')

        file_name = f'{self.get_file_name()}.vcf'

        with open(file_name, 'w') as f:
            vcf_file = File(f)
            for elt in vcfLines:
                vcf_file.write(f'{elt}\n')
        return vcf_file

    def build_qrcode(self):
        """
        With segno module (https://github.com/heuer/segno),
        generate a QrCode in PNG format.

        error='H' -> 30% error marging

        scale=10  -> indicate the size of a single module.
        For PNGs, the scaling factor is interepreted as pixel-size
        (1 = 1 pixel)

        border=4  -> size of the quiet zone (4 is recommended in segno doc)

        (Could use `.show()` instead of save: saves image as temporary file
        and opens it with the standard PNG viewer application.)

        Returns:
            File: a qr code file redirecting to Vcard file link.
        """

        file_name = f'qr_{self.get_file_name()}.png'

        qrurl = segno.make_qr(f'{self.vcf.url}', error="H")
        qrurl.save(
            out=file_name,
            kind="png",
            compresslevel=9,
            scale=10,
            border=4
            )

        if Storage.exists(self.logo.name):
            self.embed_logo_into_qrcode()
        else:
            with Image.open(file_name) as f:
                qr_file = File(f)
            return qr_file

    def embed_logo_into_qrcode(self):
        """
        With PILLOW module (https://github.com/python-pillow/Pillow),
        embed a logo into a QrCode.

        Returns:
            File: a qr code file embeded with logo,
            redirecting to Vcard file link.
        """

        qr_path = f'{self.qrcode.path}'
        logo_path = f'{self.logo.path}'

        img = Image.open(qr_path)
        width = img.size
        logo_size = 100

        current_logo = Image.open(logo_path)

        # Calculate xmin, ymin, xmax, ymax
        # to put the logo at the center of the qrcode
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        current_logo = current_logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(current_logo, (xmin, ymin, xmax, ymax))
        img.save(qr_path)
        with Image.open(qr_path) as f:
            qr_file = File(f)
        return qr_file

    def __str__(self):
        return self.get_file_name()

    class Meta:
        unique_together = ('name_first', 'name_last', 'organization')
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
