from django.db import models
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename): 
    """
    File will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    """
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class VCard(models.Model):
    """
    Vcard model.
    """
    title = models.CharField(
        _("Title"),
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
    image = models.ImageField(
        _("Image"),
        blank = True,
        max_length = 200,
        default="",
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
