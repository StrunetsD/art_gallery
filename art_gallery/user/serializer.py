from rest_framework import serializers
from .models import ClientUser, User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def validate(self, data):
            user = authenticate(username=data['username'], password=data['password'])
            if user is None:
                raise AuthenticationFailed('Invalid username or password')
            refresh = RefreshToken.for_user(user)
            return {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password1 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = ClientUser
        fields = (
            'username', 
            'password', 
            'password1',
        )

    def create(self, validated_data):
        password = validated_data['password']
        password1 = validated_data['password1']
        if password != password1:
            raise serializers.ValidationError({"password": "The two password fields must match."})   
        user = User.objects.create_user(
            username=validated_data['username'],
            password=password,
            role=User.Role.CLIENT,
        )
        refresh = RefreshToken.for_user(user)

        user.access = str(refresh.access_token)
        user.refresh = str(refresh)
        return user