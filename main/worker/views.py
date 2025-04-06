import datetime
from audioop import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import F, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from worker.forms import UserForm
from worker.models import Auto, Sales, UserProfile
from django.contrib.auth import login


# Create your views here.
class IndexDetailView(DetailView):
    model = UserProfile
    template_name = 'worker/index.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'


class AutoListView(ListView):
    model = Auto
    template_name = 'worker/auto.html'
    context_object_name = 'auto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['pk'] = pk
        return context

    def get_queryset(self):
        return Auto.objects.filter(is_sell=False)  # не проданные авто


def sell_auto(request, pk: int, auto_id: int):
    try:
        auto = Auto.objects.get(id=auto_id)
        auto.is_sell = True
        Sales.objects.create(
            worker_id=pk, auto_id=auto_id, date=datetime.datetime.now(),
            really_cost=auto.selling_price
        )
        auto.save()
    except Exception:
        return render(
            request,
            "worker/error_sell_auto.html",
            {"pk": pk, "error": "Произошла ошибка! Пожалуйста, попробуйте позже."}
        )
    url = reverse_lazy('worker:auto', kwargs={'pk': pk})
    return redirect(url)


class AccountDetailView(DetailView):
    model = UserProfile
    template_name = "worker/account.html"
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

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


from django.contrib.auth import authenticate


# ==============================================================================

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'worker/login.html'

    def form_valid(self, form):
        print("Форма валидна")

        user = form.get_user()
        if user is not None:
            print("Пользователь прошёл аутентификацию:", user.username)
        else:
            print("Пользователь не прошёл аутентификацию")

        return super().form_valid(form)

    def form_invalid(self, form):
        print("Форма НЕ валидна")
        print("Ошибки формы:", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            # Проверяем, существует ли user.id перед реверсом
            if user.id:
                return reverse_lazy('worker:index', kwargs={'pk': user.id})
            else:
                return reverse('worker:login')  # Если нет id, возвращаем на страницу логина
        else:
            return reverse('worker:login')  # Если пользователь не аутентифицирован


# ==============================================================================


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
