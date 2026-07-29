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
        if conexao:
            conexao.close()        

# a conexão falha e o finally chama uma coisa que não existe. (COREÇÃO: adicionar um if para o finally chamar uma coisa que existe)        