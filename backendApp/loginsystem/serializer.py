from rest_framework import serializers
from loginsystem.models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('id', 'fullname','email','password',)