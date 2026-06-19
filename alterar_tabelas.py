import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()


cursor.execute(''' ALTER TABLE alunos ADD COLUMN
               endereco TEXT
               ''')

cursor.execute(''' ALTER TABLE alunos ADD COLUMN
                cidade TEXT
               ''')

cursor.execute(''' ALTER TABLE alunos ADD COLUMN
               estado TEXT
               ''')
conexao.commit()
conexao.close()