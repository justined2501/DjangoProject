from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('news/', include('news.urls')),
    path('auto/', include('auto.urls')),
]
