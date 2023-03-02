from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Coche(object):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


def view_home(request):
    resultado = 1
    return render(request, 'home.html', {"result":resultado})


def view_buscar(request):
    mensaje = f"Información enviada: {request.GET['time1']}"
    resultado = request.GET['time1']
    return render(request, 'home.html', {"result": resultado})
    # return HttpResponse(mensaje)

    # return render(request, 'plantillaHeredadaHija.html', {"nombre_persona": nombre})


