from django.db import models

# Create your models here.

class Escuderia(models.Model):
 nombre= models.CharField(max_length=18)
 victorias= models.IntegerField()
 
class Piloto(models.Model):
    name= models.CharField(max_length=30)
    edad= models.IntegerField()
    podios=models.IntegerField()
   
    
class GrandPrix(models.Model):
    Pais=models.CharField(max_length=20)
    win=models.CharField(max_length=20)