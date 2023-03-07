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

        # Times
        self.barTime = "-"
        self.circuitTime = "-"
        self.raceTime = "-"
        self.raceTimeMin = "-"
        self.raceTimeSec = "-"

        # Intervals
        self.barInterval = "-"
        self.circuitInterval = "-"
        self.raceInterval = "-"

        # Grades
        self.barGrade = "-"
        self.circuitGrade = "-"
        self.raceGrade = "-"
        self.totalGrade30 = "-"
        self.totalGrade10 = "-"

        # Strings
        self.strRaceTime = "-"
        self.strBarGrade = "-"
        self.strCircuitGrade = "-"
        self.strRaceGrade = "-"
        self.strTotalGrade30 = "-"
        self.strTotalGrade10 = "-"

    def set_bar_time(self, time):
        self.barTime = int(time)
    def set_circuit_time(self, time):
        self.circuitTime = int(time)
    def set_race_time(self, timeMin, timeSec):
        self.raceTime = int(timeMin) * 60 + int(timeSec)
        self.raceTimeMin = int(self.raceTime // 60)
        self.raceTimeSec = int(self.raceTime % 60)
        strRaceTimeMin = str(self.raceTimeMin)
        strRaceTimeSec = str(self.raceTimeSec) if self.raceTimeSec>9 else "0" + str(self.raceTimeSec)
        self.strRaceTime = strRaceTimeMin + ":" + strRaceTimeSec
    def calc_all(self):
        self.calc_bar_grade()
        self.calc_circuit_grade()
        self.calc_race_grade()
        self.calc_total_grade()
        self.calc_bar_interval()
        self.calc_circuit_interval()
        self.calc_race_interval()
    def calc_bar_grade(self):
        self.barGrade = 0
        for i in range(len(Tests.arrBarTimes)):
            if self.barTime >= Tests.arrBarTimes[i]:
                self.barGrade = i + 1
        self.strBarGrade
    def calc_circuit_grade(self):
        self.circuitGrade = 0
        for i in range(len(Tests.arrCircuitTimes)):
            if self.circuitTime <= Tests.arrCircuitTimes[i]:
                self.circuitGrade = i + 1
        self.strCircuitGrade = str(self.circuitGrade) + "/10"
    def calc_race_grade(self):
        self.raceGrade = 0
        for i in range(len(Tests.arrRaceTimes)):
            if self.raceTime <= Tests.arrRaceTimes[i]:
                self.raceGrade = i + 1
        self.strRaceGrade = str(self.raceGrade) + "/10"
    def calc_total_grade(self):
        self.totalGrade30 = self.barGrade + self.circuitGrade + self.raceGrade
        self.totalGrade10 = int(self.totalGrade30/3) if self.totalGrade30%3 == 0 else round(self.totalGrade30/3, 1)
        self.strTotalGrade = str(self.totalGrade30) + "/30 (" + str(self.totalGrade10) + "/10)"
    
    def calc_bar_interval(self):
        if not self.barGrade:
            self.barInterval = f"[0 - {Tests.arrBarTimes[0]-1}]"
        elif self.barGrade != 10:
            self.barInterval = f"[{Tests.arrBarTimes[self.barGrade-1]} - {Tests.arrBarTimes[self.barGrade]-1}]"
        else:
            self.barInterval = f"[{Tests.arrBarTimes[9]} - Inf.]"
    def calc_circuit_interval(self):
        if not self.circuitGrade:
            self.circuitInterval = f"[{round(Tests.arrCircuitTimes[0]+0.1,1)} - Inf.]"
        elif self.circuitGrade != 10:
            self.circuitInterval = f"[{Tests.arrCircuitTimes[self.circuitGrade-1]} - {round(Tests.arrCircuitTimes[self.circuitGrade]-0.1,1)}]"
        else:
            self.circuitInterval = f"[0 - {Tests.arrCircuitTimes[9]}]"
    def calc_race_interval(self):
        if not self.raceGrade:
            self.raceInterval = f"[{Tests.arrRaceTimes[0]//60}:{Tests.arrRaceTimes[0]%60} - Inf.]"
        elif self.raceGrade != 10:
            self.raceInterval = f"[{Tests.arrRaceTimes[self.raceGrade-1]//60}:{Tests.arrRaceTimes[self.raceGrade-1]%60} - {Tests.arrRaceTimes[self.raceGrade]//60}:{Tests.arrRaceTimes[self.raceGrade]%60-1}]"
        else:
            self.raceInterval = f"[0 - {Tests.arrRaceTimes[9]//60}:{Tests.arrRaceTimes[9]%60}]"
    """ def set_strings(self):
        strRaceTimeMin = str(self.raceTimeMin)
        strRaceTimeSec = str(self.raceTimeSec) if self.raceTimeSec>9 else "0"+str(self.raceTimeSec)
        self.strRaceTime = strRaceTimeMin+":"+strRaceTimeSec """

def view_home(request):    
    if request.method != "POST":
        global tests
        tests = Tests()
        """ tests.set_bar_time(0)
        tests.set_circuit_time(0)
        tests.set_race_time(0, 0) """
        """ tests.calc_bar_grade()
        tests.calc_circuit_grade()
        tests.calc_race_grade()
        tests.calc_total_grade() """
    else:
        tests.set_bar_time(request.POST['timeBar'])
        tests.set_circuit_time(request.POST['timeCircuit'])
        tests.set_race_time(request.POST['timeRaceMin'], request.POST['timeRaceSec'])
        tests.calc_all()
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
