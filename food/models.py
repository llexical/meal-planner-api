from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class FoodCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imported_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Food Categories"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    bring_id = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, blank=True, null=True)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imported_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name