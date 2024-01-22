from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),

    path('listar_aluno', views.listarAluno, name='listar_aluno'),
    path('listar_curso', views.listarCurso, name='listar_curso'),
]