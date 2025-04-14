from .models import User, Profile

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'username': {'required': True,'allow_blank': False},
            'email': {'required': True,'allow_blank': False},
            'password': {'required': True,'allow_blank': False,'min_length': 8},
            }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'location', 'birth_date')
        read_only_fields = ('user',)