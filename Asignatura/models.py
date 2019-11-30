from django.db import models
from Alumno_Profesor.models import Profesor

from Alumno_Profesor.models import Alumno

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    hora_inicial = creation_date = models.TimeField( null=False)
    hora_final = creation_date = models.TimeField( null=False)

    profesores = models.ManyToManyField(Profesor, related_name="asignaturas",through='Asignaturaship') 
    alumnos = models.ManyToManyField(Alumno, related_name="asignaturas",through='Alumnosship')
    

    creation_date = models.DateTimeField(auto_now=True, null=False)
    delete = models.BooleanField(default=False)
    class Meta:
        db_table = "Asignatura"


class Asignaturaship(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True, null=False)
    delete = models.BooleanField(default=False)
    class Meta:
        db_table = "Asignaturas_profesores"



class Alumnosship(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now=True, null=False)
    delete = models.BooleanField(default=False)
    class Meta:
        db_table = "Asignaturas_alumnos"







