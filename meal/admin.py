from django.contrib import admin

from .models import Meal, FoodItem, ShoppingListItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
  list_display = ("name", "created_at", "updated_at")
  search_fields = ("name",)

class ShoppingListItemInline(admin.TabularInline):
    model = ShoppingListItem
    extra = 0
    min_num = 1
    autocomplete_fields = ['food_item']

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
  list_display = ("id", "date", "name", "created_at", "updated_at")
  search_fields = ("date", "name")
  inlines = [
    ShoppingListItemInline
  ]