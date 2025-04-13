from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import AuthenticatedAutoListView, UserProfileDetailView, ShopListView, UserCreateView, UserLoginView, UserProfileUpdateView,NewsView

urlpatterns = [
    path('<int:pk>/', AuthenticatedAutoListView.as_view(), name="auto_list_view"),
    path('news/<int:pk>/', NewsView.as_view(), name='news'),
    path('<int:pk>/account', UserProfileDetailView.as_view(), name="account"),
    path('<int:pk>/shop', ShopListView.as_view(), name="shop"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('create/', UserCreateView.as_view(), name="create"),
    path('account/edit/', UserProfileUpdateView.as_view(), name='edit'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
