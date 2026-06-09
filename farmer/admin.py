from django.contrib import admin
from .models import Farmer, Farmer_profile,Products

# Register your models here.
admin.site.register(Farmer)

admin.site.register(Farmer_profile)

admin.site.register(Products)

