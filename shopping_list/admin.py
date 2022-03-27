from django.contrib import admin

from .models import ShoppingList

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ("name", "bring_id", "created_at", "updated_at")
    search_fields = ("name", "bring_id")