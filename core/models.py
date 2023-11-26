from django.db import models

class Sala(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    
    def __str__(self):
        return str(self.numero)
    

class Municipalidad(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre
    
class Instructor(models.Model):
    rut = models.CharField(max_length=9)
    nombre_apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_ins = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_apellido
    
class Inscripcion(models.Model):
    fecha_inicio = models.CharField(max_length=50)
    fecha_termino = models.CharField(max_length=50)
    cupos = models.IntegerField()

    def __str__(self):
         return str(f'fecha inicio: {self.fecha_inicio} fecha termino: {self.fecha_termino} cupos: {self.cupos}')

    

class Taller(models.Model):
    nombre = models.CharField(max_length=50)
    horas = models.IntegerField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    municipalidad = models.ForeignKey(Municipalidad, on_delete=models.CASCADE)
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    


