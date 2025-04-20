from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from account.forms import UserProfileCreateForm, UserProfileUpdateForm
from account.models import UserProfile


class UserProfileCreateView(CreateView):
    model = UserProfile
    template_name = "account/create.html"
    form_class = UserProfileCreateForm

    def get_success_url(self):
        return reverse_lazy('account:login')


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = "account/detail.html"
    context_object_name = 'user'


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'account/update.html'
    context_object_name = 'user'
    form_class = UserProfileUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account:detail')


class UserProfileLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse_lazy('auto:list')
