from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from .forms import CustomUserUpdateForm


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
 

def update_account(request, user_id):
    if request.user.id != user_id:
      
        return redirect('index') 

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'update/update.html', {'form': form})



