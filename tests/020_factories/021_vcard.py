
from qr_vcard.factories import VCardFactory


def test_factory(db):
    """
    Factory should correctly create a new object without any errors
    """
    instance = VCardFactory(title="foo")
    assert instance.title == "foo"
