from django.contrib import admin
from cursos.models import Cursos, CursosAdmin, Estudiantes, EstudiantesAdmin
# Register your models here.

admin.site.register(Cursos, CursosAdmin)
admin.site.register(Estudiantes, EstudiantesAdmin)