from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, loader, context
from inicio.models import Escuderia, GrandPrix, Piloto
from inicio.form import CrearEscuderia, CrearGrandPrix, CrearPiloto,BuscarEscuderia, BuscarGrandPrix, BuscarPiloto, ModificarPrix
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    




   
@login_required
def pilotos(request):
    
    formulario=BuscarPiloto(request.GET)
    if formulario.is_valid():
        name_buscar = formulario.cleaned_data['name']
        listado_pilotos= Piloto.objects.filter(name__icontains=name_buscar)
    else:
       print('No es válido')
       print(name_buscar)
    return render(request,'inicio/pilotos.html',{'formulario':formulario, 'pilotos':listado_pilotos})


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



#CBV

# def grand(request):
#     diccionario = {}
    
#     if request.method == "POST":
#         formulario=CrearGrandPrix(request.POST)
#         if formulario.is_valid():
#             info=formulario.cleaned_data
#             prix=GrandPrix(pais=info["pais"],win=info["win"], descripcion=info["descripcion"])
#             prix.save()
#             diccionario["prix"] = prix
#             return redirect('prixs')
#         else:
#             diccionario["formulario"] = formulario
#             return render(request,'inicio/grand.html', diccionario)
        
    
    
#     formulario= CrearGrandPrix()
#     diccionario["formulario"] = formulario
#     return render(request,'inicio/grand.html', diccionario)

# def prixs(request):
    
#     formulario=BuscarGrandPrix(request.GET)
#     if formulario.is_valid():
#         pais_buscar = formulario.cleaned_data['pais']
#         listado_prixs= GrandPrix.objects.filter(pais__icontains=pais_buscar)
#     else:
#        print('No es válido')
#        print(pais_buscar)
#     return render(request,'inicio/prixs.html',{'formulario':formulario, 'prixs':listado_prixs})
   

    

# def eliminar_prix(request, prix_id):
#     prix= GrandPrix.objects.get(id=prix_id)
#     prix.delete()
#     return redirect('prixs')


# def modificar_prix(request,prix_id):
#     prix_modificar= GrandPrix.objects.get(id=prix_id)
    
#     if request.method == 'POST':
#        formulario = ModificarPrix(request.POST)
#        if formulario.is_valid():
#            info= formulario.cleaned_data
#            prix_modificar.pais= info['pais']
#            prix_modificar.win= info['win']
#            prix_modificar.descripcion= info['descripcion']
#            prix_modificar.save()
#            return redirect ('prixs')
#        else:
#            return render (request, 'inicio/modificar_prix.html',{'formulario':formulario} )
    
    
#     formulario = ModificarPrix(initial={'pais': prix_modificar.pais,'win': prix_modificar.win })
    
#     return render (request, 'inicio/modificar_prix.html',{'formulario':formulario} )


class CrearPrix(LoginRequiredMixin,CreateView):
    model=GrandPrix
    template_name='inicio/CBV/crear_prix_CBV.html'
    fields= ['pais','win','descripcion','autor','fecha','avatar']
    success_url= reverse_lazy('prixs')
    
class ListaPrix(ListView):
    model = GrandPrix
    template_name = "inicio/CBV/lista_prix_CBV.html"
    context_object_name= 'prixs'
    
    def get_queryset(self):
        listado_prixs=[]
        formulario=BuscarGrandPrix(self.request.GET)
        if formulario.is_valid():
          pais_buscar = formulario.cleaned_data['pais']
          listado_prixs= GrandPrix.objects.filter(pais__icontains=pais_buscar)
        
        return listado_prixs
    
    def get_context_data(self, **kwargs):
       contexto= super().get_context_data(**kwargs)
       contexto['formulario'] = BuscarGrandPrix
       
       return contexto


class ModificarPrix(LoginRequiredMixin,UpdateView):
    model = GrandPrix
    template_name = "inicio/CBV/modificar_prix_CBV.html"
    fields= ['pais','win','descripcion']
    success_url= reverse_lazy('prixs')
    
    
class EliminarPrix(LoginRequiredMixin,DeleteView):
    model = GrandPrix
    template_name = "inicio/CBV/eliminar_prix_CBV.html"
    success_url= reverse_lazy('prixs')

class MostrarPrix(DetailView):
    model = GrandPrix
    template_name = "inicio/CBV/mostrar_prix_CBV.html"




def about(request):
    return render(request,'inicio/about.html')




# Create your views here.
