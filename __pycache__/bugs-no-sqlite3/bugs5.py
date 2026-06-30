import sqlite3

def vincular_aluno_turma():
    nome = input("nome do aluno: ")
    try:
        id_turma = int(input("digite o id numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("erro no banco de dados!")
    except sqlite3.Error:
        print("erro no tipo de digitação")
    finally:
        conexao.close()    

# esta faltando um except para identificar erro quando digita frase e vez de número.        