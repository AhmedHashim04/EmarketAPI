
# import pytest
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.contrib.auth.models import User
# from account.models import Profile
# from rest_framework.authtoken.models import Token

# @pytest.fixture
# def user_with_profile():
#     # إنشاء مستخدم جديد مع بروفايل
#     user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
#     profile = Profile.objects.create(user=user, bio="Test Bio")
#     token = Token.objects.create(user=user)
#     return user, profile, token

# @pytest.mark.django_db
# def test_get_profile(user_with_profile):
#     user, profile, token = user_with_profile
#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
#     response = client.get('/api/v1/profile/')  # تغيير الرابط بما يتناسب مع URL الفيو

#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['bio'] == profile.bio
#     assert response.data['user'] == user.username

# @pytest.mark.django_db
# def test_update_profile(user_with_profile):
#     user, profile, token = user_with_profile
#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
#     new_data = {
#         'bio': "Updated Bio"
#     }
    
#     response = client.put('/api/v1/profile/', new_data, format='json')  # تغيير الرابط بما يتناسب مع URL الفيو
    
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['bio'] == "Updated Bio"

# @pytest.mark.django_db
# def test_unauthenticated_user_cannot_access_profile():
#     client = APIClient()
    
#     response = client.get('/api/v1/profile/')  # تغيير الرابط بما يتناسب مع URL الفيو
    
#     assert response.status_code == status.HTTP_401_UNAUTHORIZED

# @pytest.mark.django_db
# def test_authenticated_user_can_access_own_profile(user_with_profile):
#     user, profile, token = user_with_profile
#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
#     response = client.get('/api/v1/profile/')  # تغيير الرابط بما يتناسب مع URL الفيو
    
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['bio'] == profile.bio
