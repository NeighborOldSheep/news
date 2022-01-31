from django import forms 
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser 
        fields = ['username','email','age','password']

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser 
        fields = ['username','email','age','password']