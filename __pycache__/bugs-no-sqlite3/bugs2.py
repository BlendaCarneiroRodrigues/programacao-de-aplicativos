import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    try:
        conexao.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)",
                       (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("erro: escola inexistente!")
    finally:
        conexao.close()

# no código não tem o Foreign Key para chaves estrangeiras, então o código não reconhece a chave como existente.            