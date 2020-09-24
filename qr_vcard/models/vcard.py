from os import makedirs
from os.path import join

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

import segno


def create_folder(chemin):
    try:
        makedirs(chemin, exist_ok=True)
    except OSError as error:
        print("Directory can not be created")
        raise error


class VCard(models.Model):
    """
    [summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """

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
        upload_to=f'logos/{organization}/',
        blank=True,
        max_length=100,
        default="",
    )

    def get_full_name(self):
        """
        [summary]

        Returns:
            [type]: [description]
        """
        return f"{self.name_first} {self.name_last}"

    def get_file_name(self):
        """
        [summary]

        Returns:
            [type]: [description]
        """
        return f"{self.name_first}-{self.name_last}-{self.organization}"

    def build_vcf(self):
        """
        [summary]
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
            f'LOGO:{self.logo}',
            'END:VCARD',
            ]

        directory = 'vcf'
        dir_parent = settings.MEDIA_ROOT
        file_name = f'{self.get_file_name()}.vcf'
        path = join(dir_parent, directory)
        create_folder(path)
        full_path = join(path, file_name)

        with open(full_path, 'w') as f:
            for elt in vcfLines:
                f.write(f'{elt}\n')

    def build_qrcode(self):
        """
        [summary]
        """

        directory = 'qr_codes'
        dir_parent = settings.MEDIA_ROOT
        file_name = f'{self.get_file_name()}.png'
        path = join(dir_parent, directory)

        create_folder(path)

        full_path = join(path, file_name)

        qrurl = segno.make_qr('a link to the vcf file', error="H")
        qrurl.save(
            out=full_path,
            kind="png",
            compresslevel=9,
            scale=10,
            border=2
            )
    """
        # open qrcode image to put the logo
        img = Image.open(full_path)
        width = img.size
        # resize logo
        logo_size = 100

        # Open the logo image

        path_logo = ''.join(dir_parent, )
        un_logo = Image.open(f'{self.logo.path}')

        # Calculate xmin, ymin, xmax, ymax
        # to put the logo at the center of the qrcode
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        un_logo = un_logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(un_logo, (xmin, ymin, xmax, ymax))

        # save the qr_code
        img.save(full_path)
    """

    def __str__(self):
        """
        [summary]

        Returns:
            [type]: [description]
        """
        return self.get_file_name()

    class Meta:
        """
        [summary]
        """
        unique_together = ('name_first', 'name_last', 'organization')
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
