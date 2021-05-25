from django.shortcuts import render
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics, response, status, views, serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class RegisterAPIView(generics.GenericAPIView):
  serializer_class = UserSerializer
  
  def post(self, request):
  
    serializer = self.get_serializer(data  = request.data)
    if serializer.is_valid():
      serializer.save();
      return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class LoginAPIView(views.APIView):
  serializer_class = LoginSerializer
  def post(self, request):
    serializer = self.serializer_class(data = request.data)
    if serializer.is_valid():
      info = serializer.save()
      serialized =  UserSerializer(info['user'])
      res = {
        'token': info['access'],
        'user': serialized.data
      }
      return response.Response(res, status=status.HTTP_200_OK)
    
    
    return response.Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    