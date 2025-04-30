from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='auto:list', permanent=True)),
    path('account/', include('account.urls')),
    path('news/', include('news.urls')),
    path('auto/', include('auto.urls')),
    path('charity/', include('charity.urls')),

]
