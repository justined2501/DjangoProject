from django.contrib import admin
from django.urls import path, include
from .views import AutoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AutoListView.as_view(), name="auto_list"),
    path('worker/', include(('worker.urls', 'worker'))),
    path('moderator/', include('moderator.urls')),
]
