from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, *args, **kwargs):
        if not username:
            raise ValueError("Users must have username")
        user = self.model(username=username, *args, **kwargs)
        user.set_password(password)
        print(user)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **other_fields):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=512, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True) 
    username = models.CharField(max_length=255,unique=True, blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS=[]
    USERNAME_FIELD='username'





