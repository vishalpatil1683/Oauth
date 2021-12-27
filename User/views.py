import string

from django.shortcuts import render
from django.conf import settings
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer,UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
import random
# Create your views here.
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from .models import CustomUser
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class Register(APIView):
    permission_classes = [AllowAny]

    # def get_tokens_for_user(self,user):
    #     refresh = AccessToken.for_user(user)
    #     return {
    #         'refresh': str(refresh)
    #     }

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED,data=new_user)

        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [AllowAny]

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        JWT_token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return JWT_token

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User Not Found')
        if not user.check_password(password):
            raise AuthenticationFailed('Password Not Matched')
        is_auth = authenticate(email=email,password=password)
        if is_auth:
            JWT_TOKEN = self.get_tokens_for_user(user)
            # user = login_serializer.validate(login_serializer)
            return Response({"status": status.HTTP_200_OK, "JWT": JWT_TOKEN})
        else:
            return Response({"status": status.HTTP_404_NOT_FOUND, "MSG":'User Not Found' })


# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
class Login_Oauth(APIView):
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        JWT_token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return JWT_token

    def get(self, request, *args, **kwargs):
        # print(request.user)
        user = CustomUser.objects.filter(email=request.user).first()
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=10))
        user.is_active = True
        user.set_password(res)
        user.save()
        is_auth = authenticate(email=request.user, password=res)
        if is_auth:
            user_serializer = UserSerializer(request.user)
            if user_serializer.is_valid:
                data = {
                    "JWT":get_tokens_for_user(user),
                    "user":user_serializer.data
                }
                # print(data)
                return Response(data=data, template_name='index.html')

# def Login_Oauth(request):
#     print("Call Aya")
#     data = None
#     # print(request)
#     # print(request.get_full_path())
#     if request.user.is_authenticated:
#         request.user.is_active = True
#         JWT_TOKEN = get_tokens_for_user(request.user)
#         print(JWT_TOKEN)
#         data = {"status": status.HTTP_200_OK, "JWT": JWT_TOKEN}
#         return Response(data=data,template_name='index.html')
#         # return render(request, template_name='index.html')
#     return Response(data=data,template_name='index.html')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    JWT_token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return JWT_token