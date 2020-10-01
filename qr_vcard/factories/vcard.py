# -*- coding: utf-8 -*-
import factory

from qr_vcard.models.vcard import VCard


def fakir(data_type: str):
    return factory.Faker(data_type)


class VCardFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instance of a VCard.
    """
    organization = fakir("company")
    name_first = fakir("first_name")
    name_last = fakir("last_name")
    mobile_pers = fakir("phone_number")
    mobile_pro = fakir("phone_number")
    mail_pers = fakir("email")
    mail_pro = fakir("company_email")
    web_site = fakir("url")
    logo = factory.django.ImageField(color='blue')

    class Meta:
        model = VCard
