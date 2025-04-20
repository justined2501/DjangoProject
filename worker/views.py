from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from worker.forms import UserProfileForm, UserProfileUpdateForm
from worker.models import Sales, UserProfile


class NewsView(TemplateView):
    template_name = 'worker/news.html'
    context_object_name = 'news'

