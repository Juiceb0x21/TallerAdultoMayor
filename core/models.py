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
    

class Taller(models.Model):
    nombre = models.CharField(max_length=50)
    horas = models.IntegerField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    municipalidad = models.ForeignKey(Municipalidad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    


