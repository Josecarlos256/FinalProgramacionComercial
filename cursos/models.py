from django.db import models
from django.contrib import admin
from django.db.models.base import Model

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    carnet = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    alumnos = models.ManyToManyField(Alumnos, through='Levarcursos')

    def __str__(self):
        return self.nombre

class Llevarcursos(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)


class LlevarcursosInLine(admin.TabularInline):
    model = Llevarcursos
    extra = 1 