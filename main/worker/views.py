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
from django.views.generic import ListView, DetailView, CreateView, FormView

from worker.forms import UserForm
from worker.models import Auto, Sales, UserProfile
from django.contrib.auth import login


# Create your views here.
class StartPage(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'worker/index.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'
    login_url = 'worker:login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('worker:login')
        return super().dispatch(request, *args, **kwargs)


class AutoListView(ListView):
    model = Auto
    template_name = 'main/welcomepage.html'
    context_object_name = 'auto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Auto.objects.filter(is_sell=False)
        return Auto.objects.none()


# не проданные авто

# class SellAutoView(View):
#



class AccountDetailView(DetailView):
    model = UserProfile
    template_name = "worker/account.html"
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

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
    pk_url_kwarg = 'pk'

    def get_queryset(self, **kwargs):  # будет фильтровать продажи в будущем
        pass


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'worker/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse_lazy('worker:index', kwargs={'pk': self.request.user.pk})


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
        return reverse_lazy('worker:index', kwargs={'pk': self.object.id})
