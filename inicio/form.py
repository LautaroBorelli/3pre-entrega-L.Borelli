from django import forms


class CrearEscuderia(forms.Form):
    nombre=forms.CharField(max_length=20)
    victorias=forms.IntegerField()


class BuscarEscuderia(forms.Form):
    nombre=forms.CharField(max_length=20, required= False)
    
class BuscarGrandPrix(forms.Form):
    pais=forms.CharField(max_length=20, required= False)
    
class BuscarPiloto(forms.Form):
    name=forms.CharField(max_length=20, required= False)
  

    
class CrearGrandPrix(forms.Form):
    pais=forms.CharField(max_length=20)
    win=forms.CharField(max_length=20)
    descripcion=forms.CharField()

class CrearPiloto(forms.Form):
    name= forms.CharField(max_length=30)
    edad= forms.IntegerField()
    podios=forms.IntegerField()
    
    
class ModificarPrix(forms.Form):
    pais=forms.CharField(max_length=20)
    win=forms.CharField(max_length=20)
    descripcion=forms.CharField(max_length=199)