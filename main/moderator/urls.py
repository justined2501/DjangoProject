
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.moderator, name="moderator"),
    path('shop/', views.shop, name="shop"),

]