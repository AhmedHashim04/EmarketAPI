
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/account/', include('account.urls')),
    path('api/products/', include('product.urls')),

]


handler404 = 'utils.error_handling.handle_not_found404'
handler500 = 'utils.error_handling.handle_server_error500'
handler400 = 'utils.error_handling.handle_bad_request400'
handler403 = 'utils.error_handling.handle_permission_denied403'
handler405 = 'utils.error_handling.handle_method_not_allowed405'
handler406 = 'utils.error_handling.handle_not_acceptable406'
handler409 = 'utils.error_handling.handle_conflict409'
handler410 = 'utils.error_handling.handle_gone410'
