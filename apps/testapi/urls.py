from django.urls import path 
from testapi import views

urlpatterns = [
    path(r'/', views.index, name='index')
]