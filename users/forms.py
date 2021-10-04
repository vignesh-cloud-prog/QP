from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    name = forms.CharField(label = ("Name"))
    class Meta:
        model= User
        fields=['username','name','email','password1','password2']
        error_messages = {
            'username': {
                'unique': ("A user with that username already exists. If it's you goto login"),
            },
        }


