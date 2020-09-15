
from qr_vcard.models.card import VCard


def test_basic(db):
    """
    Basic model saving with required fields should not fail
    """
    instance = VCard(
        title="Foo",
    )
    instance.save()

    assert 1 == VCard.objects.filter(title="Foo").count()
    assert "Foo" == instance.title
