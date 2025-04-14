
from django.urls import path , include
from account.views.auth import register ,forget_password , reset_password
from account.views.profile import ProfileView


app_name = 'account'

urlpatterns = [
    # Authentication & Passwords
    path('register/', register, name='register'),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/<str:token>/', reset_password, name='reset_password'),

    # Profile
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    # Optional: Browsable API login
    path('auth/', include('rest_framework.urls')),
]

# POST    /api/token/               # Login - Get access & refresh token
# POST    /api/token/refresh/      # Refresh access token


# POST    /api/v1/account/register/
# POST    /api/v1/account/forget-password/
# POST    /api/v1/account/reset-password/<token>/

# GET     /api/v1/account/profile/<id>/

# GET     /api/v1/account/auth/     # browsable API login (optional)
# GET     /api/v1/products/                         # List products
# GET     /api/v1/products/<product_id>/            # Product detail
# POST    /api/v1/products/create/                  # Create product
# PUT     /api/v1/products/<product_id>/update/     # Update product
# DELETE  /api/v1/products/<product_id>/delete/     # Delete product

# # Reviews
# POST    /api/v1/products/<product_id>/reviews/create/
# PUT     /api/v1/products/<product_id>/reviews/<review_id>/update/
# DELETE  /api/v1/products/<product_id>/reviews/<review_id>/delete/

# # User-based
# GET     /api/v1/products/user_products
# GET     /api/v1/products/user/reviewed/
# GET     /api/v1/products/user/reviewed/<product_id>/
# GET     /api/v1/products/user/reviewed/<product_id>/rating_comment/
# GET     /api/v1/products/user/reviews/

# GET     /api/v1/orders/order/
# GET     /api/v1/orders/order/<id>/
# PUT     /api/v1/orders/order/<id>/update/
# DELETE  /api/v1/orders/order/<id>/delete/
