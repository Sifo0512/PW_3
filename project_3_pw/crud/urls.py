from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detalle/<int:id_equipo>/',views.vista_detalle,  name='detalleEquipo')
]