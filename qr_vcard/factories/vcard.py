# -*- coding: utf-8 -*-
import factory

from ..models import VCard


class VCardFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instance of a VCard.
    """
    title = factory.Faker("text", max_nb_chars=42)

    class Meta:
        model = VCard
