from django.shortcuts import render

def moderator(request):
    return render(request, "moderator/index.html")
def shop(request):
    return render(request, "moderator.html")