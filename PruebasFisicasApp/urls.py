from django.urls import path
from PruebasFisicasApp.views import view_home

urlpatterns = [
    path('home/', view_home),
    # path('buscar/', view_buscar),
]