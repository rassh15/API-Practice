import imp
from urllib import response
from django.shortcuts import render

# Create your views here.
from messageup.serializers import MessageSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from messageup.models import Message
from django.http import Http404

User = get_user_model() #to get used details stored

'''
First you have to login and generate token
and pass token in header along with the data.
This api view will create message.
To access this view you can use url (/create) 
with the form data in format
(
    {
        msg : 'Message to be sent'
    }
)

'''

class CreateMessage(APIView):
    #This will tell django we are using Token Authentication
    authentication_classes = [TokenAuthentication]
    #To restrict user and allow only authenticated user to access this website.
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def post(self, request, format=None):
        #Instancetiating serializer class with data
        serializer = self.serializer_class(data = request.data, context = {'request': request})
        #Printing data on the cosole
        print(" request ", self.request.user)
        #Creating user object to get user information
        user = User.objects.get(username=self.request.user)
        #Validationg serializer
        if serializer.is_valid():
            serializer.save()
            #extract the data from the serializer by using data attribute to get the data
            serialized_data = serializer.data
            #creating response accordingly
            response = {
                'serialized_data':serialized_data,
                'userid': str(user.id),
                'username':str(user),
                'Email':str(user.email),
            }
            # Return the serailized data as response to the API get request
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

'''
First you have to login and generate token
and pass token in header along with the data
This api view will update message.
To access this view you can use url (/<int:pk>).
Here you provide message id to access that message
with the form data in format
(
    {
        msg : 'Message to be sent'
    }
)

'''
class UpdateMessage(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    #Using this function to get correct object using primary
    #Return object if found else Error
    def get_object(self, pk):
        try:
            obj = Message.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Message.DoesNotExist:
            raise Http404
    #retrieve particular item from the list and can update it.
    def put(self, request, pk, format=None):
        
        mdata = self.get_object(pk)
        serializer = self.serializer_class(mdata, data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)


