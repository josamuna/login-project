from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Login
from .serializer import LoginSerializer

# Create your views here.
@api_view(['GET'])
def getLogin(request):
    # Get all record from Login class data
    login = Login.objects.all()
    # Serialize getting data to be formatted
    serializer = LoginSerializer(login, many=True)
    # Return serialized data (json format)
    return Response(serializer.data)

@api_view(['POST'])
def postRegisterUser(request):
    # Serialize data to add
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # return a serialized data (json format)
    return Response(serializer.data)
