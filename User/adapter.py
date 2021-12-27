from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.shortcuts import redirect,resolve_url
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken

class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):

        assert request.user.is_authenticated()
        JWT_TOKEN = get_tokens_for_user(request.user)
        print(JWT_TOKEN)
        url = settings.LOGIN_REDIRECT_URL
        return resolve_url(url)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    JWT_token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return JWT_token