from django.db import models

# Create your models here.
class ParticipantesTorneo(models.Model):
    partid = models.IntegerField()
    partnombre = models.CharField(max_length=20)
    partapellido = models.CharField(max_length=20)
    partpuntaje = models.IntegerField()
    partjugadas = models.IntegerField() 
    partcat = models.CharField(max_length=1)

class PeliculasRecomendadas(models.Model):
    pelinombre = models.CharField(max_length=50)
