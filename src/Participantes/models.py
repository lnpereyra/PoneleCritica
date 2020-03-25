from django.db import models

# Create your models here.
class ParticipantesTorneo(models.Model):
    partid = models.IntegerField(null=True)
    partnombre = models.CharField(max_length=20,verbose_name='Nombre')
    partapellido = models.CharField(max_length=20,verbose_name='Apellido')
    partpuntaje = models.IntegerField(null=True)
    partjugadas = models.IntegerField(null=True) 
    partcat = models.CharField(max_length=1,verbose_name='Categoria')

class PeliculasRecomendadas(models.Model):
    pelinombre = models.CharField(max_length=50)
