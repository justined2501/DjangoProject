import datetime
from audioop import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import F, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, TemplateView

from worker.forms import UserForm, UserEditForm
from worker.models import Auto, Sales, UserProfile
from django.contrib.auth import login


# Create your views here.
class AuthenticatedAutoListView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'main/list_auto.html'
    context_object_name = 'user'

class NewsView(TemplateView):
    template_name = 'worker/news.html'
    context_object_name = 'news'

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'worker/edit.html'
    context_object_name = 'user'
    form_class = UserEditForm

    def get_object(self, queryset = None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('worker:account', kwargs={'pk': self.object.pk})




#Профиль
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "worker/detail.html"
    context_object_name = 'user'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.pk != kwargs.get('pk'):
            return HttpResponseForbidden("Доступ запрещен.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        profite = 0
        sales_qs = Sales.objects.filter(worker_id=pk)
        for sale in sales_qs:
            profite += sale.really_cost
        context['profite'] = profite
        return context



class ShopListView(ListView):
    model = Sales
    template_name = "worker/shop.html"
    context_object_name = 'shop'




class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'worker/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse_lazy('worker:auto_list_view', kwargs={'pk': self.request.user.pk})


class UserCreateView(CreateView):
    model = UserProfile
    template_name = "worker/create.html"
    form_class = UserForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.count_of_sold_cars = 0
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('worker:auto_list_view', kwargs={'pk': self.object.id})
