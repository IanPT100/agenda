from django.shortcuts import render, redirect
from django.http import HttpResponse
from teste.forms import AlunoForm
from teste.forms import CursoForm
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

def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')


    form = AlunoForm()
    return render(request, 'incluir_aluno.html',
                  {'form': form})

def editarAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    return render(request, 'incluir_aluno.html', {'form': form})    

def incluir_cursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'incluir_cursos.html', {'form': form})

def editarCurso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(instance=curso)

    return render(request, 'incluir_cursos.html', {'form': form})

def excluirAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listar_aluno')

def excluirCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('listar_curso')
    