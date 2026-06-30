import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?,?,?)", (nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()

# se o id_prof não existir e ocorrer o erro a linha do conexao.close() não será executada.