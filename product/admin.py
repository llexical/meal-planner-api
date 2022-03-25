from django.contrib import admin
from meal_planner_api.admin import ReadOnlyAdmin
from .models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


class ProductInline(ReadOnlyAdmin, admin.TabularInline):
    model = Product
    extra = 0
    min_num = 1

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "product_count", "created_at", "updated_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        ProductInline
    ]
