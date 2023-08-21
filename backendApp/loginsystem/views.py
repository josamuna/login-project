from loginsystem.models import Login
from loginsystem.serializer import LoginSerializer
from rest_framework import viewsets

class LoginViewset(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Login.objects.all()


# from rest_framework.generics import (
#     ListAPIView, 
#     RetrieveAPIView, 
#     CreateAPIView, 
#     UpdateAPIView, 
#     DestroyAPIView)

# class LoginListView(ListAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer

# class LoginDetailView(RetrieveAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer

# class LoginCreateView(CreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer

# class LoginUpdateView(UpdateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer

# class LoginDeleteView(DestroyAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer