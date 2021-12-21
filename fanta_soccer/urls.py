from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('auction/', include('auction.urls')),
    path('tournament/', include('tournament.urls')),
    path('', include('fanta_soccer_app.urls')),
]
