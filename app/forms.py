from django import forms
from app.models import *
from django.contrib.auth.models import User

class FormDemo(forms.Form):
    image=forms.ImageField()

class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserPortfolio
        fields=('address','profile_pic')
