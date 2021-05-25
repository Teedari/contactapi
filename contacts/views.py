from django.shortcuts import render
from rest_framework import generics,status, permissions
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact


# Create your views here.

class ContactCreateAPI(generics.ListCreateAPIView):
  serializer_class = ContactSerializer
  permission_classes = (permissions.IsAuthenticated,)
  
  def perform_create(self, serializer):
    serializer.save(owner = self.request.user);
    
  def get_queryset(self):
    return Contact.objects.filter(owner=self.request.user)

  
class ContactDetailAPI(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ContactSerializer
  
  def get_queryset(self):
    return Contact.objects.filter(owner=self.request.user)
