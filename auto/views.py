from django.shortcuts import render
from django.views.generic import ListView

from auto.models import Auto


class AutoListView(ListView):
    model = Auto
    template_name = 'auto/list.html'
