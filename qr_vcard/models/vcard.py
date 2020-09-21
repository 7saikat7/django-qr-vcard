from django.db import models
from django.db.models import Value as V
from django.utils.translation import gettext_lazy as _


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
    title = name_first, name_last, organization

    def get_full_name(self):
        return self.name_first+' '+self.name_last
    
    def get_file_name(self):
        return self.name_first+'-'+self.name_last+'-'+self.organization
    
    def build_vcf(self):
        vcfLines = [
            'BEGIN:VCARD',
            'VERSION:4.0',
            f'FN:{self.get_full_name}',
            f'EMAIL;TYPE=work:{self.mail_pro}',
            f'EMAIL;TYPE=home:{self.mail_pers}',
            f'TEL;TYPE=work:{self.mobile_pro}',
            f'TEL;TYPE=home:{self.mobile_pers}',
            f'ORG:{self.organization}',
            f'URL:{self.web_site}',
            f'LOGO:{self.logo}',
            'END:VCARD',
            ]
        with open(f'{self.get_file_name}.vcf',
                  'w') as f:
            for elt in vcfLines:
                f.write(elt)
                f.write('\n')

    
    def __str__(self):
        return str(self.title)

    class Meta:
        unique_together = ('name_first', 'name_last', 'organization')
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
