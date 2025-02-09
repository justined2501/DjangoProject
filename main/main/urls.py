
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('worker/',include('worker.urls')),
    path('', views.welcomepage, name="welcomepage"),
    path('moderator/', include('moderator.urls')),

]
