import sqlite3

def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome))
    conexao.commit()


# A conexão está fora da função isso não causa erro imediato, mais prejudica na hora dos testes, para resolver é só colocar a conexão dentro sa função.