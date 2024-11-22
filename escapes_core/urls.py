"""
URL configuration for escapes project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('testportal.urls', namespace='testportal')),
    path('api/', include('testportal_api.urls', namespace='testportal_api')),
]
