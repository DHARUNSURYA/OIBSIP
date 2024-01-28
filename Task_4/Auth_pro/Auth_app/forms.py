from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class uss(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter User Name'
    }))
    email=forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Email',
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Password'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Conform Password'
    }))    
        
    class Meta:
        model=User
        fields=['username','email','password1','password2']