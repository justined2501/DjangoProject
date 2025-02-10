import datetime

from django.db.models import F, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from worker.forms import UserForm
from worker.models import Auto, Sales, User


# Create your views here.
def index(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "worker/index.html", {'user': user})


def auto(request, user_id):
    auto = Auto.objects.filter(is_sell=False)
    return render(request, "worker/auto.html", {'auto': auto, "user_id": user_id})


def sell_auto(request, user_id: int, auto_id: int):
    try:
        auto = Auto.objects.get(id=auto_id)
        auto.is_sell = True
        Sales.objects.create(
            worker_id=user_id, auto_id=auto_id, date=datetime.datetime.now(),
            really_cost=auto.selling_price
        )
        auto.save()
    except Exception:
        return render(
            request,
            "worker/error_sell_auto.html",
            {"user_id": user_id, "error": "Произошла ошибка! Пожалуйста, попробуйте позже."}
        )
    url = reverse_lazy('worker:auto', kwargs={'user_id': user_id})
    return redirect(url)


def account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profit = 0
    sales_qs = Sales.objects.filter(worker_id=user_id)
    for sales in sales_qs:
        profit += sales.really_cost


    return render(request, "worker/account.html", {'user': user, "profit": profit})


def shop(request, user_id):
    shop = Sales.objects.all
    return render(request, "worker/shop.html", {'shop': shop})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(name=username)
            return redirect('worker:index', user_id=user.id)
        except User.DoesNotExist as err:
            print(err)
            return render(request, 'worker/login.html', {'error': 'User does not exist'})
    return render(request, "worker/login.html")


def create(request):
    print(request.method)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.count_of_sold_cars = 0
            user.save()
            return redirect('worker:index', user_id=user.id)
        else:
            print(form.errors)
            data = {'form': form}
            return render(request, "worker/create.html", data)
    form = UserForm()
    data = {'form': form}
    return render(request, "worker/create.html", data)

