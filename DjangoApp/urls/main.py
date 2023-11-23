from django.contrib import admin
from django.urls import path

from DjangoApp import views

urlpatterns = [
    path("home", views.home),
    path("", views.home),
    path("secondPage", views.secondPage),
    path("help", views.helpPage),
    path("admin", admin.site.urls),
    path("accessRecords", views.accessRecords),
    path("users", views.users),
]
