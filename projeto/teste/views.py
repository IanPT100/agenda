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
            return redirect('listar_cursos')  # Redirecionar para a lista de cursos após inclusão
    else:
        form = CursoForm()

    return render(request, 'incluir_cursos.html', {'form': form})