from django import forms
from basicapp.models import newUser
from django.contrib.auth.models import User

class userForms(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username', 'email', 'Password')

class userProfileInfo(forms.ModelForm):
    class Meta():
        model=newUser
        fields=('Portfolio','Picture')
