from django.db import models
from django.contrib import admin
from django.db.models.base import Model

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    carnet = models.CharField(max_length=10)
    fechanac = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    estudiantes = models.ManyToManyField(Estudiantes, through='Lleva')
    
    def __str__(self):
        return self.nombre

class Lleva (models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

class LlevaInLine(admin.TabularInline):
    model = Lleva
    extra = 1

class EstudiantesAdmin(admin.ModelAdmin):
    inlines = (LlevaInLine,)

class CursosAdmin(admin.ModelAdmin):
    inlines = (LlevaInLine,)