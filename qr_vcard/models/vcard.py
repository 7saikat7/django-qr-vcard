from django.db import models
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
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
