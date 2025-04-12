from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import AutoListView, AccountDetailView, ShopListView, UserCreateView, UserLoginView, WelcomePageForAuthorizedUser, EditProfile

urlpatterns = [
    path('<int:pk>/', WelcomePageForAuthorizedUser.as_view(), name="index"),
    path('<int:pk>/auto', AutoListView.as_view(), name="auto"),
    path('<int:pk>/account', AccountDetailView.as_view(), name="account"),
    path('<int:pk>/shop', ShopListView.as_view(), name="shop"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('create/', UserCreateView.as_view(), name="create"),
    path('account/edit/', EditProfile.as_view(), name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
