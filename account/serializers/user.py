from ..models import User, Profile

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
        fields = ('id', 'user', 'bio', 'location', 'age')
        read_only_fields = ('user',)



# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True, min_length=8)

#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError("Username already exists.")
#         return value

#     def validate_email(self, value):
#         try:
#             validate_email(value)
#         except ValidationError:
#             raise serializers.ValidationError("Enter a valid email address.")
#         return value