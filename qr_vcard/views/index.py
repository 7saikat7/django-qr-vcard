from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """
    Dummy index view
    """
    template_name = "qr_vcard/index.html"
