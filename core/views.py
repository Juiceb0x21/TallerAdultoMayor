from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def grupo_requerido(nombre_grupo):
    def decorator (view_func):
        @user_passes_test(lambda user: user.groups.filter(name='nombre_grupo').exists())
        def wrapper(requests, *args, **kwargs):
            return view_func(requests, *args, **kwargs)
        return wrapper
    return decorator

def index(request):
    return render(request, 'core/index.html')
