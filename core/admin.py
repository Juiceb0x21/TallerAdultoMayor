from django.contrib import admin
from .models import Sala
from .models import Taller
from .models import Municipalidad
from .models import Instructor
from .models import Inscripcion

# Register your models here.
admin.site.register(Sala)

admin.site.register(Taller)

admin.site.register(Municipalidad)

admin.site.register(Instructor)

admin.site.register(Inscripcion)