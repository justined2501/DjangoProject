from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import AutoListView, UserProfileDetailView, ShopListView, UserCreateView, UserLoginView, AutoListView, UserProfileUpdateView

urlpatterns = [
    path('<int:pk>/', AutoListView.as_view(), name="auto_list_view"),
    path('<int:pk>/auto', AutoListView.as_view(), name="auto"),
    path('<int:pk>/account', UserProfileDetailView.as_view(), name="account"),
    path('<int:pk>/shop', ShopListView.as_view(), name="shop"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('create/', UserCreateView.as_view(), name="create"),
    path('account/edit/', UserProfileUpdateView.as_view(), name='edit'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
