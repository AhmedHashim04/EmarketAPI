from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'order_status', 'total_amount')
    search_fields = ('user__username', 'order_status')
    list_filter = ('order_status',)
    ordering = ('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__user__username', 'product__name')
    list_filter = ('order__order_status',)
    ordering = ('-order__order_date',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('order', 'product')
    def product_name(self, obj):
        return obj.product.name
    
