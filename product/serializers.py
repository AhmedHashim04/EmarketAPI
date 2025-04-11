from rest_framework import serializers
from .models import Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']
        extra_kwargs = {
            'description': {'required': False},
            'price': {'required': True}
        }
        read_only_fields = ['id','created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment']
        extra_kwargs = {
            'product': {'required': True},
            'user': {'required': True},
            'rating': {'required': True},
            'comment': {'required': False}
        }
        read_only_fields = ['id','created_at', 'updated_at']