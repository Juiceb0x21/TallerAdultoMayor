from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    email= forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

