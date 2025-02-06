from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"worker/index.html")

def auto(request):
    return render(request, "worker/auto.html")

def account(request):
    return render(request,"worker/account.html")

def shop(request):
    return render(request, "worker/shop.html")