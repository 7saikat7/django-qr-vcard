# -*- coding: utf-8 -*-
import factory

from qr_vcard.models.vcard import VCard


def fakir(data_type: str, nbr_char: int):
    return factory.Faker(data_type,
                         max_nb_char=nbr_char)


class VCardFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instance of a VCard.
    """
    organization = fakir("company", 150)
    name_first = fakir("first_name", 150)
    name_last = fakir("last_name", 150)
    mobile_pers = fakir("phone_number", 50)
    mobile_pro = fakir("phone_number", 50)
    mail_pers = fakir("email", 254)
    mail_pro = fakir("company_email", 254)
    web_site = fakir("url", 200)
    logo = factory.django.ImageField(color='blue')

    class Meta:
        model = VCard
