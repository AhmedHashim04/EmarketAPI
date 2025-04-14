from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'total_amount')
    search_fields = ('user__username', 'status')
    list_filter = ('status',)
    ordering = ('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__user__username', 'product__name')
    list_filter = ('order__status',)
    ordering = ('-order__order_date',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('order', 'product')
    def product_name(self, obj):
        return obj.product.name
    
    