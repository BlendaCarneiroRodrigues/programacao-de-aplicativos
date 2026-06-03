import json
import os

ARQUIVO = "alunos.json"

def carregar_dados():
    with open(ARQUIVO, 'r', encoding="utf-8") as arquivo:
        json.load(arquivo)

def criar_arquivo():
    if not os.path.exists(ARQUIVO):
        open(ARQUIVO, 'w').close()

def salvar_dados(alunos):
    with open(ARQUIVO, 'w', encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

def cadastrar_aluno():
    alunos = carregar_dados()
    id_digitado = int(input("Digite o ID do aluno: "))

    for aluno in alunos:
        if aluno["id"] == id_digitado:
            print("Erro: Este ID já está em uso!")

    novo_aluno = {
        "id": id_digitado,
        "nome": input("Nome Completo: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }

    alunos.append(novo_aluno)
    salvar_dados(alunos)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    alunos = carregar_dados()

    if not alunos:
        print("Nenhum aluno cadastrado.")

    print("----LISTA DE ALUNOS----")

    for aluno in alunos:
        print(f"""
                ID: {aluno['id']}
                Nome: {aluno['nome']}
                Telefone: {aluno['telefone']}
                Turma: {aluno['turma']}
                Idade: {aluno['idade']}
                CPF: {aluno['cpf']}
                ---------------------------
            """)

def atualizar_aluno():
    alunos = carregar_dados()
    id_busca = int(input("Digite o ID do aluno que deseja atualizar: "))

       
    for aluno in alunos:
        if aluno["id"] == id_busca:
            print("\nAluno encontrado!")
            
            nome = input(f"Nome ({aluno['nome']}): ")
            telefone = input(f"Telefone ({aluno['telefone']}): ")
            turma = input(f"Turma ({aluno['turma']}): ")
            idade = input(f"Idade ({aluno['idade']}): ")
            cpf = input(f"CPF ({aluno['cpf']}): ")

            if nome:
                aluno["nome"] = nome
            if telefone:
                aluno["telefone"] = telefone
            if turma:
                aluno["turma"] = turma
            if idade:
                aluno["idade"] = int(idade)
            if cpf:
                aluno["cpf"] = cpf

            salvar_dados(alunos)

        print("Dados atualizados com sucesso!")
        return

    print("Aluno não encontrado.")

def remover_aluno():
    alunos = carregar_dados()

    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    for aluno in alunos:
        if aluno["id"] == id_busca:
            alunos.remove(aluno)
            salvar_dados(alunos)

            print("Aluno removido com sucesso!")
    print("Aluno não encontrado.")

def menu():
    criar_arquivo()
    while True:
        print(""" --- SISTEMA DE MATRÍCULA ---

                1 - Cadastrar Aluno
                2 - Listar Alunos
                3 - Atualizar Aluno
                4 - Remover Aluno
                5 - Sair

                ----------
            """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")

menu()