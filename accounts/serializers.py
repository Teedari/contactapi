from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, models, hashers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=200, min_length=4)
  password = serializers.CharField(max_length=200, min_length=8, write_only=True)
  first_name = serializers.CharField(max_length=200, min_length=2)
  last_name = serializers.CharField(max_length=200, min_length=2)
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def validate(self, args):
      if User.objects.filter(email = args['email']).exists():
        raise serializers.ValidationError({'email', {'Email already exits'}})
      

      return super().validate(args)
    
  def create(self,validated_data):
      user = User(username = validated_data.get('username'))
      user.email = user.normalize_email(user)
      user.set_password((validated_data['password']))
      user.save();
      return user;

        
      
          
    
class LoginSerializer(serializers.ModelSerializer):
  username = serializers.CharField(max_length=200)
  password = serializers.CharField(max_length=200)
  
  class Meta:
    model = User
    fields = ['username', 'password']
  
  
  def create(self, validated_data):
    username = validated_data.get('username')
    password = validated_data.get('password')
    
    user = authenticate(username=username, password=password)
    # print(f'isUser {user}')
    if user:
      refresh  = RefreshToken.for_user(user)
      models.update_last_login(user, user)
      return {
        'user': user,
        'access': str(refresh.access_token)
      }

    
    raise exceptions.AuthenticationFailed('Authentication failed, login again')