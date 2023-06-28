from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader, context
from inicio.models import Escuderia, GrandPrix, Piloto
from inicio.form import CrearEscuderia, CrearGrandPrix, CrearPiloto
def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_escuderia(request):
  
    diccionario = {}
    
    if request.method == "POST":
        formulario=CrearEscuderia(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            escuderia=Escuderia(nombre=info["nombre"],victorias=info["victorias"])
            escuderia.save()
            diccionario["escuderia"] = escuderia 
            return render(request,'inicio/escuderia.html', diccionario)
        else:
            diccionario["formulario"] = formulario
            return render(request,'inicio/escuderia.html', diccionario)
        
    
    
    formulario= CrearEscuderia()
    diccionario["formulario"] = formulario
    return render(request,'inicio/crear_escuderia.html', diccionario)

def grand(request):
    diccionario = {}
    
    if request.method == "POST":
        formulario=CrearGrandPrix(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            grand=GrandPrix(pais=info["pais"],win=info["win"])
            grand.save()
            diccionario["grand"] = grand
            return render(request,'inicio/grand.html', diccionario)
        else:
            diccionario["formulario"] = formulario
            return render(request,'inicio/grand.html', diccionario)
        
    
    
    formulario= CrearGrandPrix()
    diccionario["formulario"] = formulario
    return render(request,'inicio/grand.html', diccionario)
   

def crear_piloto(request):
  
    diccionario = {}
    
    if request.method == "POST":
        formulario=CrearPiloto(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            piloto=Piloto(name=info["name"],edad=info["edad"],podios=info["podios"])
            piloto.save()
            diccionario["piloto"] = piloto
            return render(request,'inicio/piloto.html', diccionario)
        else:
            diccionario["formulario"] = formulario
            return render(request,'inicio/piloto.html', diccionario)
        
    
    
    formulario= CrearPiloto()
    diccionario["formulario"] = formulario
    return render(request,'inicio/piloto.html', diccionario)

# Create your views here.
