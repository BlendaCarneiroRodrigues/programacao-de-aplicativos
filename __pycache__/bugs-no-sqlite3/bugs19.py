import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sisema_escola.db')
    cursor = conexao.cursor

    cursor.execute("SELECT * FROM ? WHERE id =?" (nome_tabela, id_registro))
    print(cursor.fatchone())
    conexao.close()