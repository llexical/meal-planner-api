from django.db import models

class Meal(models.Model):
  date = models.DateField()
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class FoodItem(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class ShoppingListItem(models.Model):
  food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
  meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
  note = models.CharField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


