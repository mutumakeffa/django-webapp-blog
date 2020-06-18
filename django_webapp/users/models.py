# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from common.models import BaseModel
from PIL import Image # we are importing the image library from pillow


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField('email address', unique=True)
    objects = models.Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} Profile'

    # we will override our save method so that we can compress our image
    def save(self):
        # first we will run the save method for our parent class using the super() fxn
        super().save()

        img = Image.open(self.image.path) # this will open the image of the current instance

        # let's check the size of the image and resize appropriately
        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)





