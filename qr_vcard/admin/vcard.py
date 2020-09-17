# -*- coding: utf-8 -*-
"""
VCard admin interface
"""
from django.contrib import admin

from ..models import VCard


class VCardAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'name_first',
        'name_last',
        'mobile_pers',
        'mobile_pro',
        'mail_pers',
        'mail_pro',
        'web_site',
        'logo',
        )

    # def vcfWriter(organization, first_name, last_name,
    #           phone_pers, phone_pro, email_pers,
    #           email_pro, web_site, logo):
    
    # name = first_name + ' ' + last_name
    
    # vcfLines = []
    # vcfLines.append('BEGIN:VCARD')
    # vcfLines.append('VERSION:4.0')
    # vcfLines.append(f'FN:{name}')
    # vcfLines.append(f'EMAIL;TYPE=work:{email_pro}')
    # vcfLines.append(f'EMAIL;TYPE=home:{email_pers}')
    # vcfLines.append(f'TEL;TYPE=work:{phone_pro}')
    # vcfLines.append(f'TEL;TYPE=home:{phone_pers}')
    # vcfLines.append(f'ORG:{organization}')
    # vcfLines.append(f'URL:{web_site}')
    # vcfLines.append(f'LOGO:{logo}')
    # vcfLines.append(f'END:VCARD')
    # vcfString = ''.join(vcfLines) + '\n'
    
    # return vcfString

# Registering interface to model
admin.site.register(VCard, VCardAdmin)
