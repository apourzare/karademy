from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=13, verbose_name='شماره تلفن', null=True, blank=True)
    national_id = models.CharField(max_length=10, verbose_name='کد ملی', null=True, blank=True)
