from django.urls import path
from PruebasFisicasApp import views

urlpatterns = [
    path('home/', views.view_home, name="Home"),
    path('bootstrap/', views.bootstrap),
    path('calcNota/', views.calcNota, name="CalculoNota"),
    path('calcNota2/', views.calcNota2, name="CalculoNota2"),
]