import sqlite3

def criar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTES professores (id_professor integer primary key autoincrement,
               nome_completo_professor text not null,
               materia_professor text,
               idade_professor integer,
               cpf_professor text unique not null,
               salario_professor REAL,
               nome_escola text not null
               )''')

    nome_completo = input("Digite o nome completo do professor: ")
    materia = input("Digite a matéria do professor: ")
    idade = int(input("Digite a idade do professor: "))
    cpf = input("Digite o cpf do professor: ")
    salario = float(input("Digite o salário desse professor: "))
    nome_da_escola = input("Digite o nome da escola que esse professor da aula: ")

    comando_inserir = f''' insert into professores(nome_completo, materia_professor, idade_professor, cpf_professor, salario_professor, nome_escola)
                        values ('{nome_completo}', '{materia}', '{idade}', '{cpf}', '{salario}', '{nome_da_escola}')'''

    cursor.execute(comando_inserir)
    conexao.commit()

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores")
    dados = cursor.fetchall()

    if not dados:
        print("nenhum aluno cadastrado!")

    else:
        for dado in dados:
            print(f"nome:{nome_completo [0]}")    



def alterar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_busca = int(input("Digite o id que deseja alterar: "))