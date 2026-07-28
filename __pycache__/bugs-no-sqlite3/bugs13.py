import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    print("primeiro print:", cursor.fatchall())
    print("segundo print:", cursor.fatchall())

    conexao.close()

# O primeiro print com fatchall consome todas as informações dessa forma o segundo print não mostra nada.