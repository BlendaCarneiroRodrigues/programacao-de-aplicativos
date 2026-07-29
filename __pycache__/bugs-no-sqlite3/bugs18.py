import sqlite3

def cadastrar_lista_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("beatriz", 2)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.executemany("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", lista)
    conexao.commit()
    conexao.close()
    
# está sendo usado o execute para colocar varias informações, isso causa o erro. (COREÇÃO: trocar o execute por executemany)        