from django.urls import path
from inicio import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('escuderia/crear', views.crear_escuderia, name='crear_escuderia'),
    # path('crear/grand',views.grand, name='crear_grand'),
    path('crear/piloto',views.crear_piloto, name='crear_piloto'),
    path('escuderia/', views.escuderias, name='escuderias'),
    # path('grand/',views.prixs, name='prixs'),
    path('pilotos',views.pilotos, name = 'pilotos'),
    # path('grand/eliminar/<int:prix_id>/', views.eliminar_prix, name= 'eliminar_prix'),
    # path('grand/modificar/<int:prix_id>/', views.modificar_prix, name= 'modificar_prix'),
    
    #CBV
    path('grand/',views.ListaPrix.as_view(), name='prixs'),
    path('crear/grand',views.CrearPrix.as_view(), name='crear_prix'),
    path('grand/eliminar/<int:pk>/', views.EliminarPrix.as_view(), name= 'eliminar_prix'),
    path('grand/modificar/<int:pk>/', views.ModificarPrix.as_view(), name= 'modificar_prix'),
    path('grand/mostrar/<int:pk>/', views.MostrarPrix.as_view(), name= 'mostrar_prix'),

    ]