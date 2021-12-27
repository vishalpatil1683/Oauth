from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


from django.conf import settings


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email","user_name",'password']

        def create(self,validate_data):
            password = validate_data.pop('password',None)
            user = self.Meta.model(**validate_data)
            if password is not None:
                user.set_password(password)
            user.save()
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]

