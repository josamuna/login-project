from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Login
from .serializer import LoginSerializer

# Create your views here.
@api_view(['GET'])
def getLogins(request):
    # Get all record from Login class data
    login = Login.objects.all()
    # Serialize getting data to be formatted
    serializer = LoginSerializer(login, many=True)
    # Return serialized data (json format)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    # Serialize data to add
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST) #serializer.errors(status=status.HTTP_404_NOT_FOUND)
    # return a serialized data (json format)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def login_detail(request, pk):
    if request.method == 'GET':
        try:
            serializer = Login.objects.get(id=pk)  
        except:
            return Response('The provided id does not exist!')
        serializer_data = LoginSerializer(serializer)        
        return Response(serializer_data.data)
    elif request.method == 'PUT':
        serializer = Login.objects.get(id=pk)
        serializer_data = LoginSerializer(serializer, data=request.data) 
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            serializer = Login.objects.get(id=pk).delete()
            return Response('Record removed succesfully!') #Response(status=status.HTTP_404_NOT_FOUND)  #Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('The provided id does not exist!')