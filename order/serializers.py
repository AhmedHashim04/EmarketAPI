from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']
        extra_kwargs = {
            'quantity': {'required': True},
            'price': {'required': True}
        }
        read_only_fields = ['id']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = ['id', 'city', 'address', 'postal_code', 'phone_number', 'state', 'country',
                  'profile', 'order_date', 'status', 'payment_status', 'payment_method',
                  'total_amount', 'user', 'items']
        extra_kwargs = {
            'profile': {'required': True},
            'status': {'required': True},
            'payment_status': {'required': True},
            'payment_method': {'required': True},
            'total_amount': {'required': True}
        }
        read_only_fields = ['id', 'order_date']
 