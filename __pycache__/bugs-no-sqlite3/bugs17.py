import sqlite3

def inserir_professor(nome, materia, cpf):
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
        conexao.commit()
    except sqlite3.Error:
        print("Erro: este cpf ja esta cadastrado no sistema!")
    finally:
        conexao.close()
                