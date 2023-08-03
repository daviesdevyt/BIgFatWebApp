from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    balance = models.FloatField(default=0)
    pay_link = models.CharField(max_length=255, null=True, blank=True)
    pass