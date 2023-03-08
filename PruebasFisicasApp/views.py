from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from  PruebasFisicasApp.testClass import Tests

def view_home(request):    
    if request.method != "POST":
        global tests
        tests = Tests()
    else:
        tests.set_bar_time(request.POST['timeBar'])
        tests.set_circuit_time(request.POST['timeCircuit'])
        tests.set_race_time(request.POST['timeRaceMin'], request.POST['timeRaceSec'])
        tests.calc_all()
    return render(request, 'PruebasFisicasApp/home.html', {"tests":tests})

def bootstrap(request):
    return render(request, 'PruebasFisicasApp/bootstrap.html')
