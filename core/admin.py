from django.contrib import admin
from .models import Sala
from .models import Taller
from .models import Municipalidad

# Register your models here.
admin.site.register(Sala)

admin.site.register(Taller)

admin.site.register(Municipalidad)