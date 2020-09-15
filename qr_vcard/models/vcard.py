from django.db import models
from django.utils.translation import gettext_lazy as _


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("VCard")
        verbose_name_plural = _("VCards")
