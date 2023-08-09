from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
