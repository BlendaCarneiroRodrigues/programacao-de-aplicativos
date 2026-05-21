import json 

def criar_arquivo():
    open("alunos.json", 'w').close()

def dados(dados):
    with open("alunos.json", 'r') as arquivo:
        json.dump(dados, arquivo, indent=4)

def cadastrar(dados):
    dados = dados()
    nome = input("Digite o nome do aluno: ")
    telefone = int(input("Digite o telefone do aluno: "))
    turma = input("Digite a turma do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = int(input("Digite o cpf do aluno: "))

    dados = {
        "nome": nome,
        "telefone": telefone,
        "turma": turma,
        "idade": idade,
        "cpf": cpf
    }

def listar_alunos():
    with open("alunos.json", 'r') as arquivo:
        dados = json.load(arquivo)
    print()

def atualizar_aluno():





def remover_aluno():
    with open("alunos.json", 'r') as arquivo:
        dados = json.load(arquivo)
    if 'cpf' in dados:
        del dados ['cpf']
        print("campo 'cpf removido com sucesso'")
    with open("alunos.json", 'w', encoding='uft-8') as arquivo:
        json.dump(dados, arquivo,indent=4, ensure_ascii=False)
            