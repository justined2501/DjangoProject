from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from .views import PublicAutoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worker/', include(('worker.urls', 'worker'))),
    path('', PublicAutoListView.as_view(), name="welcomepage"),
    path('moderator/', include('moderator.urls')),
]
