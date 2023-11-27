from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *
from django.contrib.auth.models import User
from django.http import Http404
from .models import Taller, Inscripcion
# Create your views here.
 
def grupo_requerido(nombre_grupo):
    def decorator (view_func):
        @user_passes_test(lambda user: user.groups.filter(name='nombre_grupo').exists())
        def wrapper(requests, *args, **kwargs):
            return view_func(requests, *args, **kwargs)
        return wrapper
    return decorator

def index(request):
    user = request.user
    usuario_inscrito = user.groups.filter(name='Inscrito').exists()

    if user.is_authenticated and usuario_inscrito:
        perfil, creado = Perfil.objects.get_or_create(usuario=user)
        talleres_inscritos = perfil.talleres_inscritos.all()
    else:
        talleres_inscritos = None

    TallerAll = Taller.objects.all()

    data = {
        'talleres_inscritos': talleres_inscritos,
        'Talleres': TallerAll,
        'usuario': usuario_inscrito,
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
    taller = Taller.objects.get(id=id)

    data = {
        'taller': taller,
        'form' : InsForm(),
    }

    if request.method == 'POST':
        formulario = InsForm(request.POST)
        if formulario.is_valid():
            rut = formulario.cleaned_data['Rut']
            nombre = formulario.cleaned_data['Nombre']
            correo = formulario.cleaned_data['Correo']
            numero = formulario.cleaned_data['Numero']

            inscripcion = Inscripcion.objects.create(
                rut=rut,
                nombre=nombre,
                correo=correo,
                numero=numero,
            )

            taller.usuarios_inscritos.add(request.user)

            taller.inscripcion = inscripcion
            taller.save()

            return redirect('index')

    return render(request, 'core/postulacion.html', data)

@login_required
def inscribirse(request, id):
    usuario = User.objects.get(id=id)
    usuario.groups.remove(1)
    usuario.groups.add(2)
    usuario.save()
    return redirect('index')

def salir(request, id):
    usuario = User.objects.get(id=id)
    usuario.groups.remove(2)
    usuario.groups.add(1)
    usuario.save()
    return redirect('index')
