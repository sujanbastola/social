from django.contrib import admin
from django.urls import path, include
from django import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('account/',include('allauth.urls')),
