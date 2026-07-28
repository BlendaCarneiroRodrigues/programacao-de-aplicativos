import sqlite3

def cadastrar_serie_seguro(nome, Id_escola):
    try:

        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_series, id_escola) VALUES (?,?)", (nome, Id_escola))
        conexao.commit()
    except sqlite3.Error as e:
        print("erro técnico:", e)
    finally:
        conexao.close()        

# No caso de falha por falta de permissão na pasta a conexão nunca será criada        