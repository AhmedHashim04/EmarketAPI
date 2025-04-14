from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']
        extra_kwargs = {
            'description': {'required': False},
            'price': {'required': True}
        }
        read_only_fields = ['id','created_at', 'updated_at']
