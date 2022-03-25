from django.db import models

from meal.models import Meal
from food.models import Food

class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal = models.ForeignKey(
        Meal,
        related_name="shopping_list_items",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient.name
