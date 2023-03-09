from django.urls import path
from PruebasFisicasApp import views

urlpatterns = [
    path('calcNotaAntiguo/', views.calcNotaAntiguo, name="calcNotaAntiguo"),
    path('bootstrapPildoras/', views.bootstrapPildoras),
    path('calcNotaPildoras/', views.calcNotaPildoras, name="CalculoNotaPildoras"),
    path('home/', views.home, name="Home"),
    path('calcNota/', views.calcNota, name="Calculo Nota"),
    path('pruebas/', views.pruebas),
    path('redirect/', views.redirect),
]