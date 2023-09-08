from django.contrib import admin
from django.urls import path
from django.urls import include
from NewsPortal.views import upgrade_me


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('NewsPortal.urls')),
    path('accounts/', include('allauth.urls')),
    path('upgrade/', upgrade_me, name='upgrade')
]
