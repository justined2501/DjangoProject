from django.contrib import admin
from django.urls import path, include
from .views import AutoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', AutoListView.as_view(), name="auto_list"),
]
