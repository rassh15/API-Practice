from urllib import response
from django.shortcuts import render

# Create your views here.
from accounts import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class RegisterAPI(APIView):
    serializer_class = serializers.UserRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
            
        if serializer.is_valid():
            user = serializer.save()

            token = Token.objects.create(user=user)

            # refresh = RefreshToken.for_user(user)

            response_data  = {
                'tokenaccess': str(token),
                'user': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)