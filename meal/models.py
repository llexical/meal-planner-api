from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from shopping_list.models import ShoppingList
from product.models import Product

class Meal(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MealItem(models.Model):
    shopping_list = models.ForeignKey(
        ShoppingList,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='shopping_list_items'
    )
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE)
    meal = models.ForeignKey(
        Meal,
        related_name="meal_items",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient.name

@receiver(post_save, sender=Meal, dispatch_uid="add_to_shopping_list")
def add_to_shopping_list(sender, instance, **kwargs):
    """
    Work out if the meal should be in a shopping list. would be good to
    make this a model method as it will be needed else where.

    Current logic is if the meal is within the next week we should its
    meal items to the relevant shopping list by working out the closest shopping
    list day.

    Honestly this whole model is pretty messy right now (the meal item stuff)
    needs rewriting. Likely as shopping list items with a join table to meal item.
    I want multiple things to be able to add to a shopping list and I want a shopping
    list to manage itself.
    """
    print('post save called', instance, flush=True)
