from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class WelcomePageView(TemplateView):
    template_name = "main/welcomepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context
