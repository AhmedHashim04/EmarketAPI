import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

# Fixture لحذف المستخدمين بعد كل اختبار
@pytest.fixture(autouse=True)
def delete_users_after_tests():
    yield  # هذا يضمن أن الكود بعد `yield` سيتم تنفيذه بعد تنفيذ كل الاختبارات
    User.objects.get(username="ahmed123").delete()  # حذف جميع المستخدمين في قاعدة البيانات بعد كل اختبار

@pytest.mark.django_db
def test_register_user_success():
    client = APIClient()
    data = {
        "username": "ahmed123",
        "email": "ahmed@example.com",
        "password": "securepassword123"
    }
    response = client.post('/api/account/register/', data, format='json')
    
    # التحقق من الاستجابة
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['message'] == "User registered successfully."
    assert User.objects.filter(username="ahmed123").exists()

@pytest.mark.xfail
@pytest.mark.django_db
def test_register_existing_user_fails():
    # Create a user to test the "username already exists" scenario
    User.objects.create_user(username="ahmed123", email="ahmed@example.com", password="securepassword123")

    client = APIClient()
    data = {
        "username": "ahmed123",  # استخدام نفس اسم المستخدم
        "email": "newemail@example.com",
        "password": "newpass123"
    }
    response = client.post('/api/account/register/', data, format='json')

    # التحقق من أن الاستجابة تحتوي على الخطأ المناسب
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'username' in response.data
    assert response.data['username'][0] == 'A user with that username already exists.'
