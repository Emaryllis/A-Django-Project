from django.shortcuts import redirect
from django.urls import path

from DjangoApp import views

app_name = 'DjangoApp'

urlpatterns = [
    path('home', lambda _: redirect('DjangoApp:home')),
    path('', views.Home, name='home'),
    path('accessRecords', views.AccessRecords, name='accessRecords'),
    path('register', views.Register, name='register'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout'),
    path('dashboard', views.Dashboard, name='dashboard'),
]
