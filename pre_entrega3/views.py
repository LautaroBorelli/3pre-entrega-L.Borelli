from django.http import HttpResponse
from django.template import Template, loader, context
from inicio.models import Escuderias

def inicio(request):
    
    template = loader.get_template('inicio.html')
    
    diccionario = {
        'mensaje': 'Hola como están',
    }
    
    renderizar_template = template.render(diccionario)
    
    return HttpResponse(renderizar_template)

def crear_escuderia(request,nombre,victorias):
    
  template = loader.get_template('crear_escuderia.html')
    
  escuderia= Escuderias(nombre=nombre, victorias=victorias)
  escuderia.save()
  diccionario = {
        'escuderia': escuderia,
       
    }
    
  renderizar_template = template.render(diccionario)
    
  return HttpResponse(renderizar_template)