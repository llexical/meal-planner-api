from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from meal_planner_api import bring_api

class Meal(models.Model):
  date = models.DateField()
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Meal)
def update_bring(sender, instance, created, **kwargs):
    shopping_list_items = instance.shopping_list_items.all()

    for item in shopping_list_items:
      bring_api.add_item(item.food_item.name, item.note)

class FoodItem(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class ShoppingListItem(models.Model):
  food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
  meal = models.ForeignKey(Meal, related_name="shopping_list_items", on_delete=models.CASCADE)
  note = models.CharField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


