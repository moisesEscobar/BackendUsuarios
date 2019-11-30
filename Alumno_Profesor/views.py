from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404

from Alumno_Profesor.models import Genero, Alumno, Profesor
from Alumno_Profesor.serializers import GeneroSerializers, AlumnoSerializers, ProfesorSerializers


#****************************************************************************************************************************
class GeneroList(APIView):
    def get(self, request, format=None):
        queryset = Genero.objects.filter(delete=False)
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroDetail(APIView):
    def get_object(self, id):
        try:
            return Genero.objects.get(pk=id,delete=False)
        except Genero.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        gender = self.get_object(id)
        if gender != False:
            serializer = GeneroSerializers(gender)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Genero.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        gender = self.get_object(id)
        if gender != False:
            serializer = GeneroSerializers(gender, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



#****************************************************************************************************************************
class AlumnoList(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete=False)
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AlumnoDetail(APIView):
    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id,delete=False)
        except Alumno.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != False:
            serializer = AlumnoSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumno.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != False:
            serializer = AlumnoSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#****************************************************************************************************************************
class ProfesorList(APIView):
    def get(self, request, format=None):
        queryset = Profesor.objects.filter(delete=False)
        serializer = ProfesorSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfesorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProfesorDetail(APIView):
    def get_object(self, id):
        try:
            return Profesor.objects.get(pk=id,delete=False)
        except Profesor.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        profesor = self.get_object(id)
        if profesor != False:
            serializer = ProfesorSerializers(profesor)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Profesor.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        profesor = self.get_object(id)
        if profesor != False:
            serializer = ProfesorSerializers(profesor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#*****************************************************************************************************************************
