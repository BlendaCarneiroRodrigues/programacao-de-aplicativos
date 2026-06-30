import sqlite3 

def criar_tabela():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   )
                   ''')

    cursor.execute('''
                   CREAT TABLE IF NOT EXISTS series (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_escola INTEGER,
                   FOREING KEY (id_escola) REFERENCES escolas (id)
                   )
                   ''')
    
    conexao.commit()
    conexao.close()


# o primeiro cursor.execute pedi a referencia de id de uma tabela que esta em branco então não tem id para referenciar.    