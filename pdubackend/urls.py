"""pdubackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),
    path(r'testapis', include('testapi.urls')),

    # enable the admin interface
    path(r'admin', admin.site.urls),
]
