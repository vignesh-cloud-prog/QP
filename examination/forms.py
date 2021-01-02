from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    name = forms.CharField(label = ("Full Name"))
    class Meta:
        model= User
        fields=['username','name','email','password1','password2']



from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Practice

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Practice
        fields = '__all__'
