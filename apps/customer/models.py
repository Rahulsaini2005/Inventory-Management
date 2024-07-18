from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(models.Model):
    USERNAME_FIELDS = 'email'
    first_name = models.CharField('First name', max_length=30, blank=True)
    last_name = models.CharField('Last name', max_length=150, blank=True)
    username = models.EmailField('username', unique=True, null=True)
    email = models.EmailField('Email Address',unique=True,null=True)

