"""
Django settings for tests
"""

from sandbox.settings.base import *

from qr_vcard.settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "TEST": {
            "NAME": join(VAR_PATH, "db", "tests.sqlite3"),  # noqa
        }
    }
}
