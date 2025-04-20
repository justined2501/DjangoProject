from django.urls import path

from news.views import NewsView

app_name = 'news'

urlpatterns = [
    path('list/', NewsView.as_view(), name='list'),
]
