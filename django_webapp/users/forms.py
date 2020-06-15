# Next, let's subclass the UserCreationForm and UserChangeForm forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm (UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name','last_name','email')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email',)