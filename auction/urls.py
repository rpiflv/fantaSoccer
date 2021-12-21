from django.urls import path
from .views import start_auction

app_name = 'auction'

urlpatterns = [
    path('', start_auction, name='start_auction')
]