import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos, INNER JOIN turma, ON alunos.id_turma = turmas.id")

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} / Turma: {linha[1]}")
    conexao.close()    

# no código está faltando o comando ON para ligar os alunos as turmas (COREÇÃO: adiciona o ON no final do execute)     