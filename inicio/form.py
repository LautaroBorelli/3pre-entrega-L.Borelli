from django import forms

class CrearEscuderia(forms.Form):
    nombre=forms.CharField(max_length=20)
    victorias=forms.IntegerField()
    
class CrearGrandPrix(forms.Form):
    Pais=forms.CharField(max_length=20)
    win=forms.CharField(max_length=20)

class CrearPiloto(forms.Form):
    name= forms.CharField(max_length=30)
    edad= forms.IntegerField()
    podios=forms.IntegerField()