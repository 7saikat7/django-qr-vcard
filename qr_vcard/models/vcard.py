import os.path

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

import segno


class VCard(models.Model):
    """
    Vcard model.
    """

    organization = models.CharField(
        _("Organization"),
        blank=True,
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
        blank = True,
        max_length = 200,
        default="",
    )
    logo = models.URLField(
        _("Logo"),
        blank = True,
        max_length = 200,
        default="",
    )

    def get_full_name(self):
        return str(self.name_first)+' '+str(self.name_last)
    
    def get_file_name(self):
        return str(self.name_first)+'-'+str(self.name_last)+'-'+str(self.organization)
    
    def build_vcf(self):
        vcfLines = [
            'BEGIN:VCARD',
            'VERSION:4.0',
            f'FN:{str(self.get_full_name())}',
            f'EMAIL;TYPE=work:{self.mail_pro}',
            f'EMAIL;TYPE=home:{self.mail_pers}',
            f'TEL;TYPE=work:{self.mobile_pro}',
            f'TEL;TYPE=home:{self.mobile_pers}',
            f'ORG:{self.organization}',
            f'URL:{self.web_site}',
            f'LOGO:{self.logo}',
            'END:VCARD',
            ]
        with open(f'{self.get_file_name()}.vcf',
                  'w') as f:
            for elt in vcfLines:
                f.write(elt)
                f.write('\n')

    def build_qrcode(self):
        
        file_name = self.get_file_name()
        completeName = settings.MEDIA_ROOT + f"qr_code/{file_name}.txt"

        qrurl = segno.make_qr('a hyperlink to the vcf file', error = "H")    ######
        qrurl.save(out = f'qr_{completeName}.png', kind = "png", compresslevel = 9, scale = 10, border = 2)

        # open png image to put the logo
        img = Image.open(f'qr_{completeName}.png')
        width = img.size

        # How big the logo we want to put in the qr code png
        logo_size = 100

        # Open the logo image
        un_logo = Image.open('link to logo image .png')

        # Calculate xmin, ymin, xmax, ymax to put the logo at the center of the qrcode
        xmin = ymin = int((width / 2) - (logo_size / 2))
        xmax = ymax = int((width / 2) + (logo_size / 2))

        # resize the logo as calculated
        un_logo = un_logo.resize((xmax - xmin, ymax - ymin))

        # put the logo in the qr code
        img.paste(un_logo, (xmin, ymin, xmax, ymax))

        # save the qr_code
        img.save(f'{completeName}')
    
    def __str__(self):
        return str(self.name_first)+'-'+str(self.name_last)+'-'+str(self.organization)

    class Meta:
        unique_together = ('name_first', 'name_last', 'organization')
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
