from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView
from worker.models import Auto, Sales


class PublicAutoListView(ListView):
    model = Auto
    template_name = 'main/list_auto.html'
    context_object_name = 'auto'





