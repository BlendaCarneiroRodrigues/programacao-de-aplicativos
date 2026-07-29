import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(''' 
                   CREAT TABLE IF NOT EXISTS turmas ( 
                   id INTERGER PRIMARY KEY AUTOINCREMENT, 
                   nome_turma TEXT, 
                   id_serie INTERGER,
                   FOREING KEY (id_serie) REFERENCES series(id)
                   )
                   ''')
    conexao.commit()
    conexao.close()

# a coluna id_serie não tinha um tipo definido para poder gerar o id. (COREÇÃO: adicionar o INTERGER na coluna id_serie)