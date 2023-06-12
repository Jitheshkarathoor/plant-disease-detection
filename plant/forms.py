from django import forms
from .import models
from django.contrib.auth.models import User




class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={
            'password':forms.PasswordInput(),
        }
        
class custform(forms.ModelForm):
    class Meta:
        model=models.regmodel
        fields=['address','contact']