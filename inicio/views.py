from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader, context
from inicio.models import Escuderia, GrandPrix

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_escuderia(request):
    print('----------------')
    print(request.POST)
    print('----------------')
    print(request.GET)
    
    diccionario = {}
    if request.method == 'POST' :
      escudo=Escuderia(nombre=request.POST['nombre' ], victorias=request.POST['victorias'])
      escudo.save()
      diccionario['escudo'] = escudo 
          
    return render(request,'inicio/crear_escuderia.html', diccionario)

def crear_grand(request):
    diccionario= {
        
    }
    return render(request,'inicio/crear_grand.html', diccionario )



# Create your views here.
