from django.contrib import admin
from .models import Product, Category
#, Cart, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Product model.
    """
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)