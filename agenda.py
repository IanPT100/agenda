class Aluno:
    def __init__(self, nome, disciplina, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.disciplina = disciplina
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

# Inicializa uma lista vazia para armazenar os alunos
alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    disciplina = input("Digite a disciplina: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    novo_aluno = Aluno(nome, disciplina, nota1, nota2, nota3, nota4)
    alunos.append(novo_aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    print("\nLista de Alunos:")
    for aluno in alunos:
        media = (aluno.nota1 + aluno.nota2 + aluno.nota3 + aluno.nota4) / 4
        situacao = "Aprovado" if media >= 7 else "Reprovado"
        print(f"Nome: {aluno.nome}, Disciplina: {aluno.disciplina}, Média: {media:.2f}, Situação: {situacao}")

def pesquisar_aluno():
    nome_pesquisa = input("Digite o nome do aluno para pesquisa: ").lower()
    for aluno in alunos:
        if aluno.nome.lower() == nome_pesquisa:
            print(f"\nInformações do Aluno {aluno.nome}:")
            print(f"Disciplina: {aluno.disciplina}")
            print(f"Nota 1: {aluno.nota1}")
            print(f"Nota 2: {aluno.nota2}")
            print(f"Nota 3: {aluno.nota3}")
            print(f"Nota 4: {aluno.nota4}")
            return
    print(f"Aluno {nome_pesquisa} não encontrado.")


def alterar_aluno(nome_alterar):
    for aluno in alunos:
        if aluno.nome.lower() == nome_alterar.lower():
            print(f"\nInformações do Aluno {aluno.nome}:")
            print(f"Disciplina: {aluno.disciplina}")
            print(f"Nota 1: {aluno.nota1}")
            print(f"Nota 2: {aluno.nota2}")
            print(f"Nota 3: {aluno.nota3}")
            print(f"Nota 4: {aluno.nota4}")

            confirmacao = input("Deseja realmente alterar este aluno? (S/N): ").lower()
            if confirmacao == "s":
                aluno.disciplina = input("Digite a nova disciplina: ")
                aluno.nota1 = float(input("Digite a nova nota 1: "))
                aluno.nota2 = float(input("Digite a nova nota 2: "))
                aluno.nota3 = float(input("Digite a nova nota 3: "))
                aluno.nota4 = float(input("Digite a nova nota 4: "))
                print("Informações alteradas com sucesso!")
            else:
                print("Alteração cancelada.")
            return
    print(f"Aluno {nome_alterar} não encontrado.")

def excluir_aluno(nome_excluir):
    for aluno in alunos:
        if aluno.nome.lower() == nome_excluir.lower():
            print(f"\nInformações do Aluno {aluno.nome}:")
            print(f"Disciplina: {aluno.disciplina}")
            print(f"Nota 1: {aluno.nota1}")
            print(f"Nota 2: {aluno.nota2}")
            print(f"Nota 3: {aluno.nota3}")
            print(f"Nota 4: {aluno.nota4}")

            confirmacao = input("Deseja realmente excluir este aluno? (S/N): ").lower()
            if confirmacao == "s":
                alunos.remove(aluno)
                print(f"Aluno {nome_excluir} excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print(f"Aluno {nome_excluir} não encontrado.")


while True:
    print("\nMenu:")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Pesquisar Aluno")
    print("4 - Alterar Aluno")
    print("5 - Excluir Aluno")
    print("9 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_aluno()
    elif escolha == "2":
        listar_alunos()
    elif escolha == "3":
        pesquisar_aluno()
    elif escolha == "4":
        nome_alterar = input("Digite o nome do aluno para alteração: ")
        alterar_aluno(nome_alterar)
    elif escolha == "5":
        nome_excluir = input("Digite o nome do aluno para exclusão: ")
        excluir_aluno(nome_excluir)
    elif escolha == "9":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")