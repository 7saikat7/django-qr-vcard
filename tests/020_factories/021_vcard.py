
from qr_vcard.factories import VCardFactory


def test_factory_full(db):
    """
    Factory should correctly create a new object with all arguments,
    without any errors.
    """
    instance = VCardFactory(
        organization="company",
        name_first="first_name",
        name_last="last_name",
        mobile_pers="phone_number",
        mobile_pro="phone_number",
        mail_pers="email",
        mail_pro="company_email",
        web_site="url",
    )
    assert instance.organization == "company"
    assert instance.name_first == "first_name"
    assert instance.name_last == "last_name"
    assert instance.mobile_pers == "phone_number"
    assert instance.mobile_pro == "phone_number"
    assert instance.mail_pers == "email"
    assert instance.mail_pro == "company_email"
    assert instance.web_site == "url"


def test_factory_required_only(db):
    """
    Factory should correctly create a new object, with required arguments only,
    without any errors
    """
    instance = VCardFactory(
        organization="company",
        name_first="first_name",
        name_last="last_name",
        mail_pro="company_email",
    )
    assert instance.organization == "company"
    assert instance.name_first == "first_name"
    assert instance.name_last == "last_name"
    assert instance.mail_pro == "company_email"


def test_factory_faker_auto_build(db):
    instance = VCardFactory()
    assert instance.organization != ""
    assert instance.name_first != ""
    assert instance.name_last != ""
    assert instance.mobile_pers != ""
    assert instance.mobile_pro != ""
    assert instance.mail_pers != ""
    assert instance.mail_pro != ""
    assert instance.web_site != ""
