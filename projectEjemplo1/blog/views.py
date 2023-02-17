from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def saludar(request, nombre):
    return HttpResponse("Hola %s bienvenido" %nombre)