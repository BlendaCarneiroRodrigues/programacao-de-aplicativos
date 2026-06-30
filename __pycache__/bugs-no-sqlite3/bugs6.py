import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fatchone()
    print(resultado)
    conexao.close()

# o sistema não estava conseguindo interpretar o código por falta de uma virgula.    