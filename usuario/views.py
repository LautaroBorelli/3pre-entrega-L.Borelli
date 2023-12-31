from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from .form import RegistroUser,EditarUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import InfoExtra

def login(request):
    
    if request.method == 'POST':
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            usuario= formulario.cleaned_data['username']
            contrasenia= formulario.cleaned_data['password']
            
            user=authenticate(username=usuario, password=contrasenia)
            
            django_login(request,user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
        
    
    formulario=AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})


def registrarse(request):
    
   if request.method == 'POST':
       formulario=RegistroUser(request.POST)
       if formulario.is_valid():
           formulario.save()
           return redirect('usuario:login')
       
       else:
            return render(request,'usuario/registro.html',{'formulario': formulario})
    
   formulario=RegistroUser()
   return render(request,'usuario/registro.html',{'formulario': formulario})

@login_required
def editar_perfil(request):
   
    if request.method == 'POST':
        formulario=EditarUser(request.POST,request.FILES,instance=request.user)
        if formulario.is_valid():
            
            avatar= formulario.cleaned_data.get('avatar')
            info_extra_user= request.user.infoextra
            if avatar:
             info_extra_user.avatar= avatar
             info_extra_user.save()
             
             
            formulario.save()
            return redirect('inicio')
        else:
            return render(request,'usuario/editar_perfil.html',{'formulario': formulario} )
    
    formulario= EditarUser(initial= {'avatar': request.user.infoextra.avatar},instance=request.user)
    return render(request,'usuario/editar_perfil.html',{'formulario': formulario} )


class EditarPass(LoginRequiredMixin,PasswordChangeView):
    template_name='usuario/editar_pass.html'
    success_url= reverse_lazy('usuario:editar')
    
    

def perfil(request):
    
 return render(request, 'usuario/perfil.html')
    
    
    