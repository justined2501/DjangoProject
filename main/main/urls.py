from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from .views import WelcomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worker/', include(('worker.urls', 'worker'))),
    path('', WelcomePageView.as_view(), name="welcomepage"),
    path('moderator/', include('moderator.urls')),
    path('sell/<int:pk>/<int:auto_id>/', views.sell_auto, name='sell_auto'),
]
