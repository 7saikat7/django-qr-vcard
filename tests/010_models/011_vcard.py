import factory
import pytest
from django.core.exceptions import ValidationError
from qr_vcard.models import VCard


def test_missing_required(db):
    """
    Basic model validation with missing required files should fail
    """
    instance = VCard()

    with pytest.raises(ValidationError) as excinfo:
        instance.full_clean()

    assert excinfo.value.message_dict == {
        "organization": ["This field cannot be blank."],
        "name_first": ["This field cannot be blank."],
        "name_last": ["This field cannot be blank."],
        "mail_pro": ["This field cannot be blank."],
    }

def test_basic(db):
    """
    Basic model validation with required fields should not fail
    """
    vcard = VCard(
        organization=factory.Faker("company"),
        name_first=factory.Faker("first_name"),
        name_last=factory.Faker("last_name"),
        mobile_pers=factory.Faker("phone_number"),
        mobile_pro=factory.Faker("phone_number"),
        mail_pers=factory.Faker("email"),
        mail_pro=factory.Faker("company_email"),
        web_site=factory.Faker("url"),
    )
    vcard.full_clean()
    vcard.save()

    assert 1 == VCard.objects.filter(name_last="last_name").count()
    assert "company" == vcard.organization
