import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(''' 
                   CREAT TABLE IF NOT EXISTS turmas ( 
                   id INTERGER PRIMARY KEY AUTOINCREMENT, 
                   nome_turma TEXT, 
                   id_serie,
                   FOREING KEY (id_serie) REFERENCES series(id)
                   )
                   ''')
    conexao.commit()
    conexao.close()

#     