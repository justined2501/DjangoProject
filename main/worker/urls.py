from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('auto', views.auto, name="auto"),
    path('account', views.account,name="account"),
    path('shop', views.shop, name="shop"),

]