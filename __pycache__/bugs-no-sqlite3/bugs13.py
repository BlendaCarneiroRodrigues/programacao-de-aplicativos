import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall

    print("primeiro print:", dados)
    print("segundo print:", dados)

    conexao.close()

# O primeiro print com fatchall consome todas as informações dessa forma o segundo print não mostra nada. (COREÇÃO: remover os prints com o fatchall)