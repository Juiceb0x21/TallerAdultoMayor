from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            usuario = f.save()
            messages.success(request, 'Cuenta Creada correctamente')
            
            login(request, usuario)

            usuario = User.objects.get(username = usuario.username)
            usuario.groups.add(1)
            usuario.save()

            return redirect('index')

    else:
        f = CustomUserCreationForm()

    return render(request, 'registro/registro.html', {'form': f})