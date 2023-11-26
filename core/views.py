from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *
# Create your views here.

def grupo_requerido(nombre_grupo):
    def decorator (view_func):
        @user_passes_test(lambda user: user.groups.filter(name='nombre_grupo').exists())
        def wrapper(requests, *args, **kwargs):
            return view_func(requests, *args, **kwargs)
        return wrapper
    return decorator

def index(request):
    TallerAll = Taller.objects.all()

    data = {
        'Talleres' : TallerAll
    }

    return render(request, 'core/index.html', data)

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def postular(request, id):
    talleresAll = Taller.objects.get(id=id)

    data = {
        'taller' : talleresAll,
        'form' : InsForm(),
    }

    if request.method == 'POST':
        formulario = InsForm(request.POST)
        if formulario.is_valid():
            Nombre = formulario.cleaned_data['Nombre']
            Email = formulario.cleaned_data['Email']
            Monto = formulario.cleaned_data['Monto']
    

    return render(request, 'core/postulacion.html', data)

