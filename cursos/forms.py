from django import forms
from .models import Estudiantes, Cursos


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ('nombre', 'descripcion', 'estudiantes')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["estudiantes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["estudiantes"].help_text = "Ingrese los estudiantes"
        self.fields["estudiantes"].queryset = Estudiantes.objects.all()