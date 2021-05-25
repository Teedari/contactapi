from .views import RegisterAPIView,LoginAPIView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 


urlpatterns = [
  path('register', RegisterAPIView.as_view(),name='register_user'),
  
  path('login', LoginAPIView.as_view(), name='login_user'),
  # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]