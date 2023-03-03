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

class Bar(object):
    arrTimes = [36, 41, 46, 52, 57, 63, 70, 78, 86, 95]
    def __init__(self, testTime):
        self.testTime = int(testTime)
        self.testGrade = 0
    def get_grade(self):
        for i in range(len(Bar.arrTimes)):
            if self.testTime >= Bar.arrTimes[i]:
                self.testGrade = i + 1
        return self.testGrade

class Circuit(object):
    arrTimes = [12.7, 12.5, 12.3, 12, 11.6, 11.2, 10.8, 10.3, 9.8, 9.3]
    def __init__(self, testTime):
        self.testTime = int(testTime)
        self.testGrade = 0
    def get_grade(self):
        for i in range(len(Circuit.arrTimes)):
            if self.testTime <= Circuit.arrTimes[i]:
                self.testGrade = i + 1
        return self.testGrade

class Race(object):
    arrTimes = [4 * 60 + 45, 4 * 60 + 36, 4 * 60 + 27,\
        4 * 60 + 18, 4 * 60 + 9, 4 * 60, 3 * 60 + 51,\
        3 * 60 + 42, 3 * 60 + 33, 3 * 60 + 24]
    def __init__(self, testTimeMin, testTimeSec):
        self.testTime = int(testTimeMin) * 60 + int(testTimeSec)
        self.testGrade = 0
    def get_grade(self):
        for i in range(len(Race.arrTimes)):
            if self.testTime <= Race.arrTimes[i]:
                self.testGrade = i + 1
        return self.testGrade

def view_home(request):
    gradeBar = None
    gradeCircuit = None
    gradeRace = None
    return render(request, 'home.html',
        {"gradeBar":gradeBar, "gradeCircuit":gradeCircuit, "gradeRace":gradeRace})


def view_buscar(request):
    barInst = Bar(request.GET['timeBar'])
    gradeBar = barInst.get_grade()
    circuitInst = Circuit(request.GET['timeCircuit'])
    gradeCircuit = circuitInst.get_grade()
    raceInst = Race(request.GET['timeRaceMin'], request.GET['timeRaceSec'])
    gradeRace = raceInst.get_grade()

    # mensaje = f"Información enviada: {request.GET['time1']}"
    # resultado = request.GET['time1']
    return render(request, 'home.html',
        {"gradeBar":gradeBar, "gradeCircuit":gradeCircuit, "gradeRace":gradeRace})

    # return HttpResponse(mensaje)

    # return render(request, 'plantillaHeredadaHija.html', {"nombre_persona": nombre})


