from django.urls import path
from .views import *

urlpatterns = [
    	path('', index, name="index"),
        path('postulacion/<id>/', postular, name="postular")
    ]