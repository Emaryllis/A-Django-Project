# Register your models here.
from importlib import import_module
from inspect import getmembers, isclass

from django.contrib import admin
from django.contrib.auth.models import User

# Registers every class in models.py to the admin site
excludedModels = [User]
modelModule = import_module('DjangoApp.models')
[admin.site.register(model) for name, model in getmembers(modelModule, isclass) if model not in excludedModels]
