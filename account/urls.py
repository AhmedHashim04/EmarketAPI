
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
    path('profile/', ProfileView.as_view(), name='profile'),

    # Optional: Browsable API login
    path('auth/', include('rest_framework.urls')),
]

# POST    /api/token/               # Login - Get access & refresh token
# POST    /api/token/refresh/      # Refresh access token


# POST    /api/account/register/
# POST    /api/account/forget-password/
# POST    /api/account/reset-password/<token>/

# GET     /api/account/profile/<id>/

# GET     /api/account/auth/     # browsable API login (optional)
# GET     /api/products/                         # List products
# GET     /api/products/<product_id>/            # Product detail
# POST    /api/products/create/                  # Create product
# PUT     /api/products/<product_id>/update/     # Update product
# DELETE  /api/products/<product_id>/delete/     # Delete product

# # Reviews
# POST    /api/products/<product_id>/reviews/create/
# PUT     /api/products/<product_id>/reviews/<review_id>/update/
# DELETE  /api/products/<product_id>/reviews/<review_id>/delete/

# # User-based
# GET     /api/products/user_products
# GET     /api/products/user/reviewed/
# GET     /api/products/user/reviewed/<product_id>/
# GET     /api/products/user/reviewed/<product_id>/rating_comment/
# GET     /api/products/user/reviews/

# GET     /api/orders/order/
# GET     /api/orders/order/<id>/
# PUT     /api/orders/order/<id>/update/
# DELETE  /api/orders/order/<id>/delete/
