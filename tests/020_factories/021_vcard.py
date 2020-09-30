
from qr_vcard.factories import VCardFactory


def test_factory(db):
    """
    Factory should correctly create a new object without any errors
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
