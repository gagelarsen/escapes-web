"""
URL configuration for escapes project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('escapes.urls', namespace='escapes')),
    path('api/', include('escapes_api.urls', namespace='escapes_api')),
]
