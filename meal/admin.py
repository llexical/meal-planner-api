from django.contrib import admin

from .models import Meal
from shopping_list.models import ShoppingListItem

class ShoppingListItemInline(admin.TabularInline):
    model = ShoppingListItem
    extra = 0
    min_num = 1
    autocomplete_fields = ('ingredient',)
    exclude = ('shopping_list',)

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "name", "created_at", "updated_at")
    search_fields = ("date", "name")
    inlines = [
        ShoppingListItemInline
    ]