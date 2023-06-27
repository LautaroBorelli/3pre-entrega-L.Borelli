from django.http import HttpResponse
from django.template import Template, loader, context


def inicio(request):
    
    template = loader.get_template('inicio.html')
    
    diccionario = {
        'mensaje': 'Hola como están',
    }
    
    renderizar_template = template.render(diccionario)
    
    return HttpResponse(renderizar_template)

