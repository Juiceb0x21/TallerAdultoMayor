from django.urls import path
from .views import *

urlpatterns = [
    	path('', index, name="index"),

        path('postulacion/<id>/', postular, name="postular"),

        path('inscribir/<id>/', inscribirse, name="inscribirse"),

        path('salir/<id>/', salir, name="salir"),

       path('eliminar_cuenta/<int:id>/', delete_account, name='delete_account'),

    ]