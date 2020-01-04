from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('go',views.go, name='go'),
    path('contact', views.contact, name='contact'),
    ]
