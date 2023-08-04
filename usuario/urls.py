from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'usuario'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('registro/',views.registrarse, name='registrarse'),
    path('perfil/',views.perfil, name='perfil'),
    path('perfil/editar/',views.editar_perfil, name='editar'),
    path('perfil/editar/pass/',views.EditarPass.as_view(), name='editar_pass')
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)