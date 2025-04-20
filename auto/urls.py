from django.urls import path

from auto.views import AutoListView

app_name = 'auto'

urlpatterns = [
    path('list/', AutoListView.as_view(), name='list'),
]
