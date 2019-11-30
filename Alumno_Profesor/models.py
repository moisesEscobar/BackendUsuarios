from django.db import models
from django.utils import timezone

class Genero(models.Model):
    name = models.CharField(max_length=100,null=False)
    creation_date = models.DateField(auto_now=True, null=False)
    delete = models.BooleanField(default=False)
    class Meta:
        db_table = "Generos"

class Alumno(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido_paterno = models.CharField(max_length=255, null=False)
    apellido_materno = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)
    direccion = models.CharField(max_length=255, null=False)
    correo_electronico = models.CharField(max_length=255, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True, null=False)

    delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = "Alumnos"


class Profesor(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido_paterno = models.CharField(max_length=255, null=False)
    apellido_materno = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)
    direccion = models.CharField(max_length=255, null=False)
    correo_electronico = models.CharField(max_length=255, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True, null=False)
    delete = models.BooleanField(default=False)
    class Meta:
        db_table = "Profesor"


    


