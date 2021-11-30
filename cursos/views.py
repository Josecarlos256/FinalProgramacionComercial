from django import forms
from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm
from cursos.models import Cursos, Estudiantes, Lleva

def curso_nuevo(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Cursos.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'])
            for estudiante_id in request.POST.getlist('estudiantes'):
                lleva = Lleva(estudiante_id=estudiante_id, curso_id = curso.id)
                lleva.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado')
    else:
        formulario = CursoForm()
    return render(request, '/curso/curso_editar.html', {'formulario': formulario})
