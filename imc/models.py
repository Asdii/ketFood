from django.db import models
from django.db.models import Avg

class ket(models.Model):
	nombre = models.CharField(max_length=150)
	peso = models.CharField(max_length=10)
	estatura = models.CharField(max_length=10)
	edad = models.CharField(max_length=5)
	sexo = models.CharField(max_length=15)

	def __str__(self):
		return self.nombre

	def contar(self):
		return self.objects.count()

	def promedioIMC(self):
		p = ket.objects.aggregate(Avg('peso'))
		e = ket.objects.aggregate(Avg('estatura'))
		imc = (sum(p.values()) / ((sum(e.values()) * sum(e.values())) / 100)) * 100
		return int(imc)