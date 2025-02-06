from django.shortcuts import render
from django.http import HttpResponse

def welcomepage(request):
    return render(request,"main/welcomepage.html")

