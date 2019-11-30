from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^asignaturas/$', views.AsignaturaList.as_view()),


    
    re_path(r'^asignaturas/(?P<id>\d+)$', views.AsignaturaDetail.as_view()),
        
    re_path(r'^Asignaturas-profesores/$', views.AsignaturashipList.as_view()),
    re_path(r'^Asignaturas-profesores/(?P<id>\d+)$',views.AsignaturashipDetail.as_view()), 

    re_path(r'^Asignaturas-alumnos/$', views.AlumnosshipList.as_view()),
    re_path(r'^Asignaturas-alumnos/(?P<id>\d+)$',views.AlumnosshipDetail.as_view()),

]