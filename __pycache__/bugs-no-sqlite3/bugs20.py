import sqlite3

def cadastrar_escolas_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO scolas (id, nome) VALUES (?,?)", (id_escola, nome))

    conexao.commit()
    conexao.close()