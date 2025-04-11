from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer , RegisterSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register(request):
    """
    Register a new user.
    """
    user = RegisterSerializer(data=request.data)
    if user.is_valid():
        if User.objects.filter(username=user.validated_data['username']).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        elif User.objects.filter(email=user.validated_data['email']).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user.save()
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
    

    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """
    Login a user.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_view(request):
    """
    Logout a user.
    """
    if request.method == 'POST':
        # Assuming you have a session-based authentication system
        logout(request)
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile 
