from rest_framework import routers, serializers

from Asignatura.models import Asignatura, Asignaturaship, Alumnosship
from Alumno_Profesor.models import Profesor
from Alumno_Profesor.models import Alumno

class ProfesorFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('__all__') 
        
class AlumnoFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__') 
        



class AsignaturaSerializers(serializers.ModelSerializer):
    alumnos = AlumnoFilterSerializers(many=True,read_only=True)
    profesores = ProfesorFilterSerializers(many=True,read_only=True)


    class Meta:
        model = Asignatura
        fields = ('__all__')








class AsignaturashipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asignaturaship
        fields = ('__all__')

class AlumnosshipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnosship
        fields = ('__all__')