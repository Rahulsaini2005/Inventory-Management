"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports

from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views


urlpatterns = [
    # admin urls
    path('', include('apps.administrator.urls')),
    # enable the admin interface
    path(r'^administration', admin.site.urls),
    # auth urls
    path('password_reset/', PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html'
    ), name='password_reset'),
    # path('', include('django.contrib.auth.urls')),
    # Ckeditor urls
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.user.urls')),
    # customer urls
    path('', include('apps.customer.urls')),
    path('', include('apps.item.urls')),
    path('', include('apps.product.urls')),
    path('', include('apps.location.urls')),
    path('api-token-auth/', views.obtain_auth_token),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
