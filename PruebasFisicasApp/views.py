from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from  PruebasFisicasApp.testClass import Tests
from django.views import View

def calcNotaAntiguo(request):    
    if request.method != "POST":
        global tests
        tests = Tests()
    else:
        tests.set_bar_time(request.POST['timeBar'])
        tests.set_circuit_time(request.POST['timeCircuit'])
        tests.set_race_time(request.POST['timeRaceMin'], request.POST['timeRaceSec'])
        tests.calc_all()
    return render(request, 'PruebasFisicasApp/calcNotaAntiguo.html', {"tests":tests})

def bootstrapPildoras(request):
    return render(request, 'PruebasFisicasApp/bootstrapPildoras.html')

def calcNotaPildoras(request):
    return render(request, 'PruebasFisicasApp/calcNotaPildoras.html')

def home(request):
    return render(request, 'PruebasFisicasApp/home.html')

def calcNota(request):
    if not request.GET:
        global tests
        tests = Tests()
        return render(request, 'PruebasFisicasApp/calcNota.html', {"tests":tests})
    elif 'calcButton' in request.GET:
        if request.GET['calcButton'] == 'bar' or request.GET['calcButton'] == 'all':
            tests.set_bar_time(request.GET['timeBar'])
            tests.calc_bar_grade()
            tests.calc_bar_interval()
        if request.GET['calcButton'] == 'circuit' or request.GET['calcButton'] == 'all':
            tests.set_circuit_time(request.GET['timeCircuit'])
            tests.calc_circuit_grade()
            tests.calc_circuit_interval()
        if request.GET['calcButton'] == 'race' or request.GET['calcButton'] == 'all':
            tests.set_race_time(request.GET['timeRaceMin'], request.GET['timeRaceSec'])
            tests.calc_race_grade()
            tests.calc_race_interval()
        """ elif request.GET['calcButton'] == 'all':
            tests.set_bar_time(request.GET['timeBar'])
            tests.set_circuit_time(request.GET['timeCircuit'])
            tests.set_race_time(request.GET['timeRaceMin'], request.GET['timeRaceSec'])
            tests.calc_all() """
        return render(request, 'PruebasFisicasApp/calcNota.html', {"tests":tests})
    else:
        print('aaa')


def pruebas(request):
    texto = "AAA"
    if request.GET:
        print("aaaaa", request.GET)
        texto = request.GET['var']
        request.GET = None
    return render(request, 'PruebasFisicasApp/pruebas.html', {"texto":texto})

def redirect(request):
    print("bbb")
    pruebas(request)

""" class AwesomeView(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if (msg) : del(request.session['msg'])
        return render(request, 'getpost/guess.html', {'message' : msg})
    def post(self, request):
        msg = request.POST.get('guess')
        request.session['msg'] = msg
        return redirect(request.path) """
