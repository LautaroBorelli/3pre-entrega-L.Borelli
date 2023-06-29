from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, loader, context
from inicio.models import Escuderia, GrandPrix, Piloto
from inicio.form import CrearEscuderia, CrearGrandPrix, CrearPiloto,BuscarEscuderia, BuscarGrandPrix, BuscarPiloto
def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_escuderia(request):
  
    
    
    if request.method == "POST":
        formulario=CrearEscuderia(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            escuderia=Escuderia(nombre=info["nombre"],victorias=info["victorias"])
            escuderia.save()
            return redirect('escuderias')
        else:
            return render(request,'inicio/crear_escuderia.html', {'formulario':formulario})
        
    
    
    formulario= CrearEscuderia()
  
    return render(request,'inicio/crear_escuderia.html',{'formulario':formulario})

def escuderias(request):
    
    formulario=BuscarEscuderia(request.GET)
    if formulario.is_valid():
        nombre_buscar = formulario.cleaned_data['nombre']
        listado_escuderias= Escuderia.objects.filter(nombre__icontains=nombre_buscar)
    else:
       print('No es válido')
       print(nombre_buscar)
    return render(request,'inicio/escuderia.html',{'formulario':formulario, 'escuderias':listado_escuderias})
    



def grand(request):
    diccionario = {}
    
    if request.method == "POST":
        formulario=CrearGrandPrix(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            prix=GrandPrix(pais=info["pais"],win=info["win"])
            prix.save()
            diccionario["prix"] = prix
            return redirect('prixs')
        else:
            diccionario["formulario"] = formulario
            return render(request,'inicio/grand.html', diccionario)
        
    
    
    formulario= CrearGrandPrix()
    diccionario["formulario"] = formulario
    return render(request,'inicio/grand.html', diccionario)

def prixs(request):
    
    formulario=BuscarGrandPrix(request.GET)
    if formulario.is_valid():
        pais_buscar = formulario.cleaned_data['pais']
        listado_prixs= GrandPrix.objects.filter(pais__icontains=pais_buscar)
    else:
       print('No es válido')
       print(pais_buscar)
    return render(request,'inicio/prixs.html',{'formulario':formulario, 'prixs':listado_prixs})
   

def crear_piloto(request):
  
    diccionario = {}
    
    if request.method == "POST":
        formulario=CrearPiloto(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            piloto=Piloto(name=info["name"],edad=info["edad"],podios=info["podios"])
            piloto.save()
            diccionario["piloto"] = piloto
            return redirect('pilotos')
        else:
            diccionario["formulario"] = formulario
            return render(request,'inicio/piloto.html', diccionario)
        
    
    
    formulario= CrearPiloto()
    diccionario["formulario"] = formulario
    return render(request,'inicio/piloto.html', diccionario)

def pilotos(request):
    
    formulario=BuscarPiloto(request.GET)
    if formulario.is_valid():
        name_buscar = formulario.cleaned_data['name']
        listado_pilotos= Piloto.objects.filter(name__icontains=name_buscar)
    else:
       print('No es válido')
       print(name_buscar)
    return render(request,'inicio/pilotos.html',{'formulario':formulario, 'pilotos':listado_pilotos})

# Create your views here.
