from django.urls import path
from inicio import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('escuderia/crear', views.crear_escuderia, name='crear_escuderia')
    path('crear/grand',views.crear_grand, name='crear_grand')
    ]