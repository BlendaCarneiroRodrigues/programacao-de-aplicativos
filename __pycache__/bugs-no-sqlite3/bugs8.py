import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREAT TABLE IF NOT EXISTS professores ( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nome TEXT, 
                   cpf TEXT UNIQUE 
                   )
                   ''')
    
# o sistema aceita dois cpf igual por que na estrutura da tabela não esta especificando que tem que ser cpf unico esta faltado o UNIQUE na tabela.    