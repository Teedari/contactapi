from django.urls import path
from .views import ContactCreateAPI, ContactDetailAPI

urlpatterns = [
  path('', ContactCreateAPI.as_view(), name='all contacts'),
  path('<int:pk>/', ContactDetailAPI.as_view(), name='detail contact')
]