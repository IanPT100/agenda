from django.shortcuts import render
from django.http import HttpResponse

from teste.models import Aluno
from teste.models import Curso



def index(request):
    return HttpResponse("pão de queijo."),

def listarAluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_aluno.html', {'alunos': alunos})

def listarCurso(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_curso.html', {'cursos': cursos})



