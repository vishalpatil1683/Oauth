from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def create_superuser(self,email,password,**other_fields):
        # if password != confirm_password:
        #     raise ValueError(_("Password are not matching"))
        user_name = email.split('@')[0]
        user = self.create_user(email=email,user_name=user_name,password=password)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError(_("Email Id Missing"))
        # if password != confirm_password:
        #     raise ValueError(_("Password are not matching"))
        email = self.normalize_email(email)
        user_name = email.split('@')[0]
        user = self.model(email=email,user_name=user_name)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    user_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email