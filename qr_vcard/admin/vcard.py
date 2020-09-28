# -*- coding: utf-8 -*-
"""
VCard admin interface
"""
from django.contrib import admin
from django.http import HttpResponse

from ..models import VCard


class VCardAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'organization',
                ('name_first', 'name_last'),
                ('mobile_pro', 'mail_pro'),
                'logo',
                )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'web_site',
                ('mobile_pers', 'mail_pers'),
                ('vcf', 'qrcode'),
                ),
        }),
    )
    readonly_fields = (
        'vcf',
        'qrcode',
        )
    list_display = (
        'get_full_name',
        'name_last',
        'organization',
        'name_first',
        'logo',
        )

    ordering = ('name_last', 'name_first')
    search_fields = ('name_last', 'organization',)


# Registering interface to model
admin.site.register(VCard, VCardAdmin)
