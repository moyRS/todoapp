from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('completar/<int:tarea_id>', views.completar_tarea, name='completar_tarea'),
    path('eliminar/<int:tarea_id>', views.eliminar_tarea, name='eliminar_tarea'),
    ]