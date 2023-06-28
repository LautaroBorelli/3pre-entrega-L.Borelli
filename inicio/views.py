from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader, context

def inicio(request):
    return render(request,'inicio/inicio.html')

def prueba(request):
    
    diccionario = {
        'mensaje': 'Hola como están',
    }    
    return render(request,'inicio/prueba.html', diccionario)

# Create your views here.
