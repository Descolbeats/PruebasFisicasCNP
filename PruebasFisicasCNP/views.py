from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Coche(object):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Grade(object):
    arr_grades = [10,20,30,40,50]
    def __init__(self, time):
        self.time = time
        self.grade = 0
    def get_grade(self):
        for i in range(len(Grade.arr_grades)):
            if self.time >= Grade.arr_grades[i]:
                self.grade = i + 1    


def view_home(request):
    resultado = 1
    return render(request, 'home.html', {"result":resultado})


def view_buscar(request):
    grade1 = Grade(int(request.GET['time1']))
    grade1.get_grade()
    result1 = str(grade1.grade)

    # mensaje = f"Información enviada: {request.GET['time1']}"
    resultado = request.GET['time1']
    return render(request, 'home.html', {"result": result1})
    # return HttpResponse(mensaje)

    # return render(request, 'plantillaHeredadaHija.html', {"nombre_persona": nombre})


