from django.contrib import admin
from .models import Player, AddItem, Contact

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['jersey_number', 'first_name', 'last_name', 'position', 'email']
    list_filter = ['position', 'state']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(AddItem)
class AddItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_price', 'item_description']
    search_fields = ['item_name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']
