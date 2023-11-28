from django.urls import path
from .views import *

urlpatterns = [

    path('', register, name="Autenticacion"),
        path('actualizar_cuenta/<int:user_id>/', update_account, name='update_account'),

]
