from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404

from Asignatura.models import Asignatura, Asignaturaship, Alumnosship
from Asignatura.serializers import AsignaturaSerializers, AsignaturashipSerializers, AlumnosshipSerializers

#****************************************************************************************************************************
class AsignaturaList(APIView):
    def get(self, request, format=None):
        queryset = Asignatura.objects.filter(delete=False)
        serializer = AsignaturaSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AsignaturaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AsignaturaDetail(APIView):
    def get_object(self, id):
        try:
            return Asignatura.objects.get(pk=id,delete=False)
        except Asignatura.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        asignatura = self.get_object(id)
        if asignatura != False:
            serializer = AsignaturaSerializers(asignatura)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Asignatura.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        asignatura = self.get_object(id)
        if asignatura != False:
            serializer = AsignaturaSerializers(asignatura, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#****************************************************************************************************************************
class AsignaturashipList(APIView):
    def get(self, request, format=None):
        queryset = Asignaturaship.objects.filter(delete=False)
        serializer = AsignaturashipshipSerializers(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AsignaturashipSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AsignaturashipDetail(APIView):
    def get_object(self, id):
        try:
            return Asignaturaship.objects.get(pk=id, delete=False)
        except Asignaturaship.DoesNotExist:
            return False
    def get(self, request, id, format=None):
        asignaturaship = self.get_object(id)
        if asignaturaship != False:
            serializer = AsignaturashipSerializers(asignaturaship)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        Asignaturaship.objects.filter(asignatura=id).delete()
        return Response("ok")
        
    def put(self, request, id, format=None):
        asignaturaship = self.get_object(id)
        if asignaturaship != False:
            asignaturaship = AsignaturashipSerializers(asignaturaship, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



#****************************************************************************************************************************
class AlumnosshipList(APIView):
    def get(self, request, format=None):
        queryset = Alumnosship.objects.filter(delete=False)
        serializer = AlumnosshipSerializers(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AlumnosshipSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnosshipDetail(APIView):
    def get_object(self, id):
        try:
            return Alumnosship.objects.get(pk=id, delete=False)
        except Alumnosship.DoesNotExist:
            return False
    def get(self, request, id, format=None):
        alumnosship = self.get_object(id)
        if alumnosship != False:
            serializer = AlumnosshipSerializers(alumnosship)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        Alumnosship.objects.filter(alumno=id).delete()
        return Response("ok")
        
    def put(self, request, id, format=None):
        alumnosship = self.get_object(id)
        if alumnosship != False:
            alumnosship = AlumnosshipSerializers(alumnosship, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
