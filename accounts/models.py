from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    phone_number=models.CharField(max_length=13,unique=True)
    otp = models.CharField(max_length=4)
    username=None
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects = UserManager()

