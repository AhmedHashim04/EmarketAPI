from django.contrib import admin
from .models import Product, Category ,Review 
#, Cart, Order, OrderItem

# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Product model.
    """
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Review model.
    """
    list_display = ('product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)