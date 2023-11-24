from django.urls import path

from DjangoApp import views

app_name = 'DjangoApp'

urlpatterns = [
    path("home", views.Home),
    path("", views.Home, name="home"),
    path("accessRecords", views.AccessRecords, name="accessRecords"),
    path("users", views.UserList, name="users"),
    path("form", views.Form, name="form"),
    path("register", views.Register, name="register"),
]
