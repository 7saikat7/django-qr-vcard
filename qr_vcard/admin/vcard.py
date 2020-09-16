# -*- coding: utf-8 -*-
"""
VCard admin interface
"""
from django.contrib import admin

from ..models import VCard


class VCardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'name_first',
        'name_last',
        'mobile_pers',
        'mobile_pro',
        'mail_pers',
        'mail_pro',
        'web_site',
        )


# Registering interface to model
admin.site.register(VCard, VCardAdmin)
