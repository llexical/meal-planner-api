from django.db import models

from meal.models import Meal
from product.models import Product

weekday_choices = (
    (0, 'Monday'),
    (1, 'Truesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday')
)

class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    bring_id = models.CharField(max_length=255, null=True, blank=True)
    day_of_the_week = models.IntegerField(null=True, blank=True, choices=weekday_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE)
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
