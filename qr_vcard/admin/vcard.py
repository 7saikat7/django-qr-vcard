# -*- coding: utf-8 -*-
"""
VCard admin interface
"""
from django.contrib import admin
from django.http import HttpResponse

from ..models import VCard


class VCardAdmin(admin.ModelAdmin):
    """
    [summary]

    Args:
        admin ([type]): [description]
    """

    list_display = (
        'get_full_name',
        'name_last',
        'organization',
        'name_first',
        'logo',
        'vcf',
        'qrcode',
        )

    ordering = ('organization',)
    search_fields = ('name_last', 'organization',)


# Registering interface to model
admin.site.register(VCard, VCardAdmin)
