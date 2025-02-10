from django.urls import path
from . import views
app_name = "moderator"
urlpatterns = [
    path('', views.moderator, name="moderator"),
    path("users", views.users, name="users"),
    path("sales", views.sales, name="sales"),
    path('shop/', views.shop, name="shop"),

]