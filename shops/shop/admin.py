from django.contrib import admin
from  .models import City, Shop, Street

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'home', 'open_shop', 'work_from', 'work_to']
    prepopulated_fields = {'slug': ('name',)}



