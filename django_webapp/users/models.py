# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from common.models import BaseModel


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField('email address', unique=True)
    objects = models.Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
