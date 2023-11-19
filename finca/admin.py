from django.contrib import admin
from .models import Propiedad

# Register your models here.
from django.contrib.admin import AdminSite

admin.register(Propiedad)