from rest_framework import routers, serializers
from Alumno_Profesor.models import Genero, Alumno, Profesor
from Asignatura.models import Asignatura

class AlumnoFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('__all__') 
class ProfesorFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('__all__') 

class AsignaturaFilterSerializers(serializers.ModelSerializer):
    profesores = ProfesorFilterSerializers(many=True,read_only=True)
    alumnos = AlumnoFilterSerializers(many=True,read_only=True)
    class Meta:
        model = Asignatura
        fields = ('__all__') 
        

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')


class AlumnoSerializers(serializers.ModelSerializer):
    asignaturas = AsignaturaFilterSerializers(many=True,read_only=True)
    sexo =  serializers.ReadOnlyField(source='genero.name')
    class Meta:
        model = Alumno
        fields = ('__all__')


class ProfesorSerializers(serializers.ModelSerializer):
    asignaturas = AsignaturaFilterSerializers(many=True,read_only=True) 
    sexo =  serializers.ReadOnlyField(source='genero.name')
    class Meta:
        model = Profesor
        fields = ('__all__') 
