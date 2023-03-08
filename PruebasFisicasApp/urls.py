from django.urls import path
from PruebasFisicasApp import views

urlpatterns = [
    path('home/', views.view_home),
    path('bootstrap/', views.bootstrap),
]