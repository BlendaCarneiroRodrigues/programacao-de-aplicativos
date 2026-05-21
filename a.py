import json
import os

ARQUIVO = "alunos.json"


# =========================
# FUNÇÕES AUXILIARES
# =========================

def carregar_alunos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def salvar_alunos(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)


# =========================
# CADASTRAR
# =========================

def cadastrar_aluno():
    alunos = carregar_alunos()

    cpf = input("CPF: ")

    # Verifica CPF duplicado
    for aluno in alunos:
        if aluno["cpf"] == cpf:
            print("Erro: já existe um aluno com esse CPF.")
            return

    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    turma = input("Turma: ")
    idade = input("Idade: ")

    novo_aluno = {
        "cpf": cpf,
        "nome": nome,
        "telefone": telefone,
        "turma": turma,
        "idade": idade
    }

    alunos.append(novo_aluno)
    salvar_alunos(alunos)

    print("Aluno cadastrado com sucesso!")


# =========================
# LISTAR
# =========================

def listar_alunos():
    alunos = carregar_alunos()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n===== LISTA DE ALUNOS =====")

    for aluno in alunos:
        print(f"""
CPF: {aluno["cpf"]}
Nome: {aluno["nome"]}
Telefone: {aluno["telefone"]}
Turma: {aluno["turma"]}
Idade: {aluno["idade"]}
----------------------------
""")


# =========================
# EDITAR
# =========================

def editar_aluno():
    alunos = carregar_alunos()

    cpf = input("Digite o CPF do aluno que deseja editar: ")

    for aluno in alunos:
        if aluno["cpf"] == cpf:

            print("Digite os novos dados:")

            aluno["nome"] = input("Novo nome: ")
            aluno["telefone"] = input("Novo telefone: ")
            aluno["turma"] = input("Nova turma: ")
            aluno["idade"] = input("Nova idade: ")

            salvar_alunos(alunos)

            print("Dados atualizados com sucesso!")
            return

    print("Aluno não encontrado.")


# =========================
# EXCLUIR
# =========================

def excluir_aluno():
    alunos = carregar_alunos()

    cpf = input("Digite o CPF do aluno que deseja excluir: ")

    for aluno in alunos:
        if aluno["cpf"] == cpf:
            alunos.remove(aluno)

            salvar_alunos(alunos)

            print(f'Aluno {aluno["nome"]} removido do sistema.')
            return

    print("Aluno não encontrado.")


# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("""
========= MENU =========
1. Cadastrar Aluno
2. Listar Alunos
3. Editar Aluno
4. Excluir Aluno
5. Sair
========================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        editar_aluno()

    elif opcao == "4":
        excluir_aluno()

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")