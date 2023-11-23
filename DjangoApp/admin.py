# Register your models here.
from importlib import import_module
from inspect import getmembers, isclass

from django.contrib import admin

# Registers every class in models.py to the admin site
module = import_module('DjangoApp.models')
members = getmembers(module, isclass)
for name, model in members: admin.site.register(model)
# END
