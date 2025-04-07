from django.urls import path
from . import views
from .views import AutoListView, AccountDetailView, ShopListView, UserCreateView, UserLoginView, UserHome

urlpatterns = [
    path('<int:pk>/', UserHome.as_view(), name="index"),
    path('<int:pk>/auto', AutoListView.as_view(), name="auto"),
    path('<int:pk>/account', AccountDetailView.as_view(), name="account"),
    path('<int:pk>/shop', ShopListView.as_view(), name="shop"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('create/', UserCreateView.as_view(), name="create"),
]
