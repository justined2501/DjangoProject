from django.views.generic import TemplateView


class DonateCarView(TemplateView):
    template_name = 'charity/donate.html'


