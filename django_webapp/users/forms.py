# Next, let's subclass the UserCreationForm and UserChangeForm forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Profile
from django import forms

class CustomUserCreationForm (UserCreationForm):
    # add any additional field

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name','last_name','email')

class CustomUserChangeForm(UserChangeForm):   #this form will help us update our email

    class Meta(UserChangeForm):
        model = User
        fields = ('first_name','last_name','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
