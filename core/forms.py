from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

class InsForm(forms.Form):
    rut= forms.CharField(label='Rut', max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre= forms.CharField(label='Nombre Completo', min_length=0, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo= forms.CharField(label='Correo', min_length=0, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero= forms.CharField(label='Telefono', min_length=0, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))


