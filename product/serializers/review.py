from rest_framework import serializers
from ..models import Product, Review



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