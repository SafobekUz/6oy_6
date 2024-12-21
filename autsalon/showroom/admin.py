from django.contrib import admin
from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'established_year')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'release_year')
    list_filter = ('brand',)
