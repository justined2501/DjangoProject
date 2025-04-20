from django.urls import path
from . import views

app_name = "moderator"
urlpatterns = [
    path('', views.moderator, name="user_detail"),
]
