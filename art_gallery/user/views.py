from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout


class UserLogoutView(GenericAPIView):
    def post(self, request):
        logout(request)
        return Response(
            {"message": "logout"},
            status=status.HTTP_200_OK,
        )
    

class UserLoginView(GenericAPIView):
    permission_classes = ()

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.validated_data
            return Response(tokens, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserRegisterView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response(
                {
                    "message": "User registered successfully",
                    "access": access_token,
                    "refresh": refresh_token
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)