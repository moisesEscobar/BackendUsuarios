from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^generos/$', views.GeneroList.as_view()),
    re_path(r'^generos/(?P<id>\d+)$', views.GeneroDetail.as_view()),
    
    re_path(r'^alumnos/$', views.AlumnoList.as_view()),
    re_path(r'^alumnos/(?P<id>\d+)$',views.AlumnoDetail.as_view()),
    re_path(r'^profesores/$', views.ProfesorList.as_view()),
    re_path(r'^profesores/(?P<id>\d+)$',views.ProfesorDetail.as_view()),  
]