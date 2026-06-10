import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute(''' create table if not exists alunos( ID_aluno integer primary key autoincrement,
                    nome_aluno text not null,
                    telefone_aluno text,
                    turma_aluno text,
                    idade_aluno integer,
                    cpf_aluno text inique not null
                    )''')

nome = input("Digite o nome do aluno: ")
telefone = input("Digite o telefote do aluno: ")
turma = input("digite a turma do aluno: ")
idade = int(input("Digite a idade do aluno: "))
cpf = input("Digite o CPF do aluno: ")

comando_inserir = f''' insert into alunos(nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno)
                        values ('{nome}', '{telefone}', '{turma}', '{idade}', '{cpf}')'''

cursor.execute(comando_inserir)
conexao.commit()
conexao.close()

print("Dados gravados com sucesso!")