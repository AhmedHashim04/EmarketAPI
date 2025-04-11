
from django.urls import path
from .views import product_list , product_detail , create_product \
, update_product , delete_product , create_review , update_review , delete_review ,user_products ,user_reviewed_product \
, user_reviewed_product_rating_comment , user_reviewed_products , user_reviews

#, product_add, product_edit, product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<str:product_id>/', product_detail, name='product_detail'),
    path('create/', create_product, name='create_product'),
    path('<str:product_id>/update/', update_product, name='update_product'),
    path('<str:product_id>/delete/', delete_product, name='delete_product'),
    path('<str:product_id>/reviews/create/', create_review, name='create_review'),
    path('<str:product_id>/reviews/<str:review_id>/update/', update_review, name='update_review'),
    path('<str:product_id>/reviews/<str:review_id>/delete/', delete_review, name='delete_review'),
    path('user_products', user_products, name='user_products'),
    path('user/reviewed/', user_reviewed_products, name='user_reviewed_products'),
    path('user/reviewed/<str:product_id>/', user_reviewed_product, name='user_reviewed_product'),
    path('user/reviewed/<str:product_id>/rating_comment/', user_reviewed_product_rating_comment, name='user_reviewed_product_rating_comment'),
    path('user/reviews/', user_reviews, name='user_reviews'),


]
