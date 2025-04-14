from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from account.serializers.user import  RegisterSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone 
from datetime import timedelta
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from account.models import Profile
@api_view(['POST'])
def register(request):
    """
    Register a new user.
    """ 
    user = RegisterSerializer(data=request.data)

    if user.is_valid():
        # التحقق أولاً من وجود اسم المستخدم
        if User.objects.filter(username=user.validated_data['username']).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # إذا لم يكن اسم المستخدم موجودًا، يتم إنشاؤه
        user = User.objects.create(
            username=user.validated_data['username'],
            email=user.validated_data['email'],
            password=make_password(user.validated_data['password']))
        
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def forget_password(request):
    """
    Handle password reset.
    """
    if request.method == 'POST':
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            # Here you would typically send an email with a password reset link
            token = get_random_string(50)  # Generate a token for password reset
            expired_data = timezone.now() + timedelta(days=1)  # Set expiration date for the token
            user.profile.reset_password_token = token
            user.profile.reset_password_expired = expired_data
            user.profile.save()

            link = f"http://{request.get_host()}/api/account/reset-password/{token}/"  # Create a link to reset the password
            body = f"Click the link to reset your password: {link}"
            send_mail(f"Password From Emarket ", body, 'ahmedha4im7@gmail.com', [email], fail_silently=False)
            user.save()

            return Response({'message':'Password reset link sent to your email.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def reset_password(request, token):
    """
    Reset the password using the token.
    """
    if request.method == 'POST':
        password = request.data.get('password')
        if not password:
            return Response({'error': 'Password is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 8:
            return Response("Password must be at least 8 characters long.")
        try:
            profile = Profile.objects.get(reset_password_token=token)
            if profile.reset_password_expired < timezone.now():
                return Response({'error': 'Token expired.'}, status=status.HTTP_400_BAD_REQUEST)

            user = profile.user
            user.set_password(password)
            profile.reset_password_token = ''
            profile.reset_password_expired = None
            profile.save()
            user.save()

            return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_404_NOT_FOUND)
    

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
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successful.', 'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Logout a user.
    """
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)

