from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.Form):
    rut= forms.CharField(label='Rut', min_length=9, max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido1 = forms.CharField(label='Primer Apellido', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido2 = forms.CharField(label='Segundo Apellido', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    fecha_nac = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label='Telefono', min_length=9, max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label='Direccion', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_rut(self):
        username = self.cleaned_data['rut'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Rut ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Correo ya existe")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['rut'],
            email=self.cleaned_data['email'],
            password= self.cleaned_data['password1'],
            first_name=self.cleaned_data['nombre'],
            last_name=self.cleaned_data['apellido1']
        )
        
        user.apellido2 = self.cleaned_data['apellido2']
        user.fecha_nac = self.cleaned_data['fecha_nac']
        user.telefono = self.cleaned_data['telefono']
        user.direccion = self.cleaned_data['direccion']


        return user
