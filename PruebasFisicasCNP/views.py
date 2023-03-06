from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

""" class Coche(object):
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
                self.grade = i + 1 """

class Tests():
    arrBarTimes = [36, 41, 46, 52, 57, 63, 70, 78, 86, 95]
    arrCircuitTimes = [12.7, 12.5, 12.3, 12, 11.6, 11.2, 10.8, 10.3, 9.8, 9.3]
    arrRaceTimes = [4 * 60 + 45, 4 * 60 + 36, 4 * 60 + 27,\
        4 * 60 + 18, 4 * 60 + 9, 4 * 60, 3 * 60 + 51,\
        3 * 60 + 42, 3 * 60 + 33, 3 * 60 + 24]
    def __init__(self):
        """ self.arrBarTimes = [36, 41, 46, 52, 57, 63, 70, 78, 86, 95]
        self.arrCircuitTimes = [12.7, 12.5, 12.3, 12, 11.6, 11.2, 10.8, 10.3, 9.8, 9.3]
        self.arrRaceTimes = [4 * 60 + 45, 4 * 60 + 36, 4 * 60 + 27,\
        4 * 60 + 18, 4 * 60 + 9, 4 * 60, 3 * 60 + 51,\
        3 * 60 + 42, 3 * 60 + 33, 3 * 60 + 24] """

        self.barTime = 0
        self.circuitTime = 0
        self.raceTime = 0

        self.barInterval = "[0 - 35]"
        self.circuitInterval = None
        self.raceInterval = None

        self.barGrade = 0
        self.circuitGrade = 0
        self.raceGrade = 0

        self.totalGrade30 = None
        self.totalGrade10 = None
    def set_bar_time(self, time):
        self.barTime = int(time)
    def set_circuit_time(self, time):
        self.circuitTime = int(time)
    def set_race_time(self, timeMin, timeSec):
        self.raceTime = int(timeMin) * 60 + int(timeSec)
    def calc_bar_grade(self):
        self.barGrade = 0
        for i in range(len(Tests.arrBarTimes)):
            if self.barTime >= Tests.arrBarTimes[i]:
                self.barGrade = i + 1
    def calc_circuit_grade(self):
        self.circuitGrade = 0
        for i in range(len(Tests.arrCircuitTimes)):
            if self.circuitTime <= Tests.arrCircuitTimes[i]:
                self.circuitGrade = i + 1
    def calc_race_grade(self):
        self.raceGrade = 0
        for i in range(len(Tests.arrRaceTimes)):
            if self.raceTime <= Tests.arrRaceTimes[i]:
                self.raceGrade = i + 1
    def calc_total_grade(self):
        self.totalGrade30 = self.barGrade + self.circuitGrade + self.raceGrade
        self.totalGrade10 = int(self.totalGrade30/3) if self.totalGrade30%3 == 0 else round(self.totalGrade30/3, 1)
    
    def calc_bar_interval(self):
        if not self.barGrade:
            self.barInterval = f"[0 - {Tests.arrBarTimes[0]}]"
        elif self.barGrade != 10:
            self.barInterval = f"[{Tests.arrBarTimes[self.barGrade]} - {Tests.arrBarTimes[self.barGrade+1]-1}]"
        else:
            self.barInterval = f"> {Tests.arrBarTimes[9]}"

            

""" class Bar():
    arrTimes = [36, 41, 46, 52, 57, 63, 70, 78, 86, 95]
    def __init__(self, testTime):
        self.testTime = int(testTime)
        self.testGrade = 0
    def get_grade(self):
        for i in range(len(Bar.arrTimes)):
            if self.testTime >= Bar.arrTimes[i]:
                self.testGrade = i + 1
        return self.testGrade

class Circuit():
    arrTimes = [12.7, 12.5, 12.3, 12, 11.6, 11.2, 10.8, 10.3, 9.8, 9.3]
    def __init__(self, testTime):
        self.testTime = int(testTime)
        self.testGrade = 0
    def get_grade(self):
        for i in range(len(Circuit.arrTimes)):
            if self.testTime <= Circuit.arrTimes[i]:
                self.testGrade = i + 1
        return self.testGrade

class Race():
    arrTimes = [4 * 60 + 45, 4 * 60 + 36, 4 * 60 + 27,\
        4 * 60 + 18, 4 * 60 + 9, 4 * 60, 3 * 60 + 51,\
        3 * 60 + 42, 3 * 60 + 33, 3 * 60 + 24]
    def __init__(self, testTimeMin, testTimeSec):
        self.testTime = int(testTimeMin) * 60 + int(testTimeSec)
        self.testGrade = 0
    def get_grade(self):
        for i in range(len(Race.arrTimes)):
            if self.testTime <= Race.arrTimes[i]:
                self.testGrade =  i + 1
        return self.testGrade """

def view_home(request):    
    if request.method != "POST":
        global tests
        tests = Tests()
        """ tests.set_bar_time(0)
        tests.set_circuit_time(0)
        tests.set_race_time(0, 0) """
        tests.calc_bar_grade()
        tests.calc_circuit_grade()
        tests.calc_race_grade()
        tests.calc_total_grade()
    else:
        tests.set_bar_time(request.POST['timeBar'])
        tests.set_circuit_time(request.POST['timeCircuit'])
        tests.set_race_time(request.POST['timeRaceMin'], request.POST['timeRaceSec'])
        tests.calc_bar_grade()
        tests.calc_circuit_grade()
        tests.calc_race_grade()
        tests.calc_total_grade()
        tests.calc_bar_interval()
    return render(request, 'home.html', {"tests":tests})

""" def view_buscar(request):
    tests.set_bar_time(request.GET['timeBar'])
    tests.set_circuit_time(request.GET['timeCircuit'])
    tests.set_race_time(request.GET['timeRaceMin'], request.GET['timeRaceSec'])
    tests.calc_bar_grade()
    tests.calc_circuit_grade()
    tests.calc_race_grade()
    tests.calc_total_grade()

    # mensaje = f"Información enviada: {request.GET['time1']}"
    # resultado = request.GET['time1']
    return render(request, 'home.html', {"tests":tests})

    # return HttpResponse(mensaje)

    # return render(request, 'plantillaHeredadaHija.html', {"nombre_persona": nombre})
 """
