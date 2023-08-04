# 3pre-entrega-L.Borelli

Esta es mi tercer entrega- Desarrollo WEB Django
Lo hice con una pantalla de inicio donde se pueden ver imagens e informacion...
En el extremo superior lo separé en Inicio - Escuderias - Grand Prix - Pilotos..
Cada uno de esos models cuenta con su pagina y su formulario, en el que puedes ver el listado de 
los objetos creados y crear más....
Los formularios los hice con form.py... 
La estetica es por herencia del 'base.html' 



Entrega Final :

Este proyecto se lleva a acabo con entorno virtual activandolo de la siguiente manera :'. venv/Scripts/activate'

Para activar el servidor ejecutamos el siguiente comando : 'python manage.py runserver'

Para añadir migraciones : 'python manage.py makemigrations'
                          'python manage.py migrate'

Para hacer commits : 'git commit -m ('mensaje')'

Este proyecto tiene una sección llamada Grand Prix que la acomodé para que parezca lo más posible a un blog... Esta consta de poner el país y ganador de una carrera, y a raíz de eso contar en un post lo que le pareció dicha carrera o lo que sintió al verla.... Además se le puede colocar fecha y nombre del autor...La descripcion se trabaja con un texto RichTextField y se le puede añadir imagen...
Cuenta con un formulario para buscar blogs por pais... También muestra botones para modificar,eliminar y ver mas...
Este proyecto tambíen cuenta con clases basadas en vista que es la que utilizo en el Grand Prix..
Tambíen cuenta con funciones tanto de Login, logout como también para editar el perfil....
Cuenta con funciones que requieren estar logueado...
Tiene un apartado de Acerca de mi en la parte inferior de la página, donde escribo breves datos de mi, aparte la información va acompañada de una imagen... 