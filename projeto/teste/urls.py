from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),

    path('listar_aluno', views.listarAluno, name='listar_aluno'),
    path('listar_curso', views.listarCurso, name='listar_curso'),
    path('incluir_aluno', views.incluirAluno, name='incluir_aluno'),
    path('editar_aluno/<int:id>', views.editarAluno, name='editar_aluno'),
    path('incluir_cursos/', views.incluir_cursos, name='incluir_cursos'),
    path('editar_curso/<int:id>', views.editarCurso, name='editar_curso'),
]