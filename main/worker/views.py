from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from worker.forms import UserForm
from worker.models import Auto,Sales,User


# Create your views here.
def index(request,user_id):
    user = get_object_or_404(User,id=user_id)
    return render(request,"worker/index.html",{'user':user})

def auto(request,user_id):
    auto = Auto.objects.all
    user = get_object_or_404(User,id=user_id)
    return render(request, "worker/auto.html",{'auto':auto})

def account(request,user_id):
    user = get_object_or_404(User,id=user_id)
    return render(request,"worker/account.html",{'user':user})

def shop(request,user_id):
    shop = Sales.objects.all
    return render(request, "worker/shop.html",{'shop':shop})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        try:
            user = User.objects.get(name=username)
            return redirect('index', user_id = user.id)
        except User.DoesNotExist:
            return render (request,'worker/login.html',{'error': 'User does not exist'})
    return render(request, "worker/login.html")

def create(request):
    print(request.method)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.count_of_sold_cars = 0
            user.save()
            return redirect('index')
        else:
            print(form.errors)
            data = {'form': form}
            return render(request, "worker/create.html", data)
    form = UserForm()
    data = {'form': form}
    return render(request, "worker/create.html",data)