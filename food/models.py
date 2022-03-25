from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

FOOD_CATEGORIES = (
    ('veg','Veg'),
    ('fruit', 'Fruit'),
    ('fresh_herbs', 'Fresh Herbs'),
    ('meat','Meat'),
    ('seafood','Seafood'),
    ('vegetarian_fresh','Vegetarian Fresh'),
    ('ready_meal', 'Ready Meal'),
    ('cold_meats', 'Cold Meats'),
    ('diary', 'Dairy'),
    ('spices_and_herbs', 'Spices & Herbs'),
    ('dry_carbs', 'Dry Carbs'),
    ('tinned', 'Tinned'),
    ('alcohol', 'Alcohol'),
    ('soft_drink', 'Soft Drinks'),
    ('snacks', 'Snacks'),
    ('bread', 'Bread'),
    ('baking', 'Baking'),
    ('eggs', 'Eggs'),
    ('frozen', 'Frozen'),
    ('household', 'Household'),
    ('toiletries', 'Toiletries')
)

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