from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    pass


class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'required': True,
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'required': True,
            'placeholder': 'Enter password'
        }
    ))
