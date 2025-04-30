from django.urls import path

from charity.views import DonateCarView

app_name = 'charity'

urlpatterns = [
    path('donate/', DonateCarView.as_view(), name='donate'),
]