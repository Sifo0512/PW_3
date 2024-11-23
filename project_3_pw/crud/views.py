from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Equipo

# Create your views here.
def index(request):
    lista_equipos = Equipo.objects.all()
    template = loader.get_template("index.html")
    context = {'equipos':lista_equipos}
    return HttpResponse(template.render(context,request))

def vista_detalle(request,id_equipo):
    detalle_equipo = Equipo.objects.get(id=id_equipo)
    template = loader.get_template('detail.html')
    context = {'equipo':detalle_equipo}
    return HttpResponse(template.render(context,request))