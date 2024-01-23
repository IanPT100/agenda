from django import forms
from django.forms import ModelForm, TextInput, Textarea
from teste.models import Aluno , Curso

 
class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


