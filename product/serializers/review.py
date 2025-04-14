from rest_framework import serializers
from ..models import Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment']
        # extra_kwargs = {
        #     'product': {'required': False},
        #     'user': {'required': False},
        #     'rating': {'required': True},
        #     'comment': {'required': False}
        # }
        # read_only_fields = ['id','created_at', 'updated_at'] 