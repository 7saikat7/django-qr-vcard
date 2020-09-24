from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from qr_vcard.views.index import IndexView

app_name = 'qr_vcard'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
