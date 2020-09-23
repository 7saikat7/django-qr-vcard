# -*- coding: utf-8 -*-
"""
VCard admin interface
"""
from django.contrib import admin

from ..models import VCard


class VCardAdmin(admin.ModelAdmin):

    def make_vcf(modeladmin, request, queryset):
        VCard.build_vcf
    make_vcf.short_description = "Make a vcf file."

    actions = [make_vcf, VCard.build_qrcode]

    list_display = (
        'name_last',
        'organization',
        'name_first',
        'mobile_pers',
        'mobile_pro',
        'mail_pers',
        'mail_pro',
        'web_site',
        'logo',
        'get_full_name',
        'build_vcf'
        )

    ordering = ('name_last',)
    search_fields = ('name_last', 'organization')
    """
    def Download_vcf(self, request, queryset):
        from django.http import HttpResponse
        VCard.build_vcf()
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

    Download_vcf.short_description = "Download .vcf file for selected contacts."
    """


# Registering interface to model
admin.site.register(VCard, VCardAdmin)
