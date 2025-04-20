from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import UserProfileLoginView, UserProfileDetailView, UserProfileCreateView, UserProfileUpdateView

app_name = 'account'

urlpatterns = [
    path('login/', UserProfileLoginView.as_view(), name='login'),
    path('create/', UserProfileCreateView.as_view(), name='create'),
    path('detail/', UserProfileDetailView.as_view(), name='detail'),
    path('update/', UserProfileUpdateView.as_view(), name='update'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
