from django.db import models
from django import forms
from ckeditor.fields import RichTextField


# Create your models here.

class Escuderia(models.Model):
 nombre= models.CharField(max_length=18)
 victorias= models.IntegerField()
 
class Piloto(models.Model):
    name= models.CharField(max_length=30)
    edad= models.IntegerField()
    podios=models.IntegerField()
   
    
class GrandPrix(models.Model):
    pais=models.CharField(max_length=20)
    win=models.CharField(max_length=20)
    autor=models.CharField( null=True,max_length=20)
    fecha=models.DateTimeField(null=True)
    descripcion=RichTextField(null=True)
    avatar= models.ImageField(upload_to='avatares',null=True,blank=True)
    def __str__(self):
        return f"País: {self.pais} -- Win: {self.win} -- Autor:{self.autor} -- fecha: {self.fecha} -- Imagen: {self.avatar}"
    
    
class InfoExtra(models.Model):
    avatar= models.ImageField(upload_to='avatares',null=True,blank=True)
