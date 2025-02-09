from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.index,name="index"),
    path('<int:user_id>/auto', views.auto, name="auto"),
    path('<int:user_id>/account', views.account,name="account"),
    path('<int:user_id>/shop', views.shop, name="shop"),
    path('login/', views.login, name="login"),
    path('create/', views.create, name="create"),

]