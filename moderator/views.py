from django.shortcuts import render


def users(request):
    pass


def sales(request):
    pass


def moderator(request):
    return render(request, "moderator/index.html")


def shop(request):
    return render(request, "moderator.html")
