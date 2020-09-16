# -*- coding: utf-8 -*-
"""
VCard admin interface
"""
from django.contrib import admin

from ..models import VCard


class VCardAdmin(admin.ModelAdmin):
    pass


# Registering interface to model
admin.site.register(VCard, VCardAdmin)
