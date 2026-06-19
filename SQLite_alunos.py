import sqlite3

def cadastrar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute(''' create table if not exists alunos( 
                   ID_aluno integer primary key autoincrement,
                nome_aluno text not null,
                telefone_aluno text,
                turma_aluno text,
                idade_aluno integer,
                cpf_aluno text inique not null,
                id_professor INTEGER,
                FOREIGN KEY (id_professor) REFERENCES PROFESSORES (id),
                endereco TEXT,   
                cidade TEXT,
                estado TEXT      
                )''')

    nome = input("Digite o nome do aluno: ")
    telefone = input("Digite o telefote do aluno: ")
    turma = input("digite a turma do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = input("Digite o CPF do aluno: ")
    id_professor = int(input("Digite o id do professor que esse aluno sera vinculado: "))
    endereco = input("Digite")


    comando_inserir = f''' insert into alunos(nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno, id_professor)
                        values ('{nome}', '{telefone}', '{turma}', '{idade}', '{cpf}', '{id_professor}')'''

    print("Dados gravados com sucesso!")
    cursor.execute(comando_inserir)
    conexao.commit()


def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    if not alunos:
       print("Nenhum aluno encontrado!")
    else:
       for aluno in alunos:
          print(f"id: {aluno[0]}, Nome: {aluno[1]}, Telefone: {aluno[2]}, Turma: {aluno[3]}, Idade: {aluno[4]}, CPF: {aluno[5]}, id_do_professor: {aluno[6]}") 
    conexao.close()        


def atualizar():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_aluno = int(input("Digite o id do aluno para atualizar: "))
    cursor.execute(f'''SELECT * FROM alunos WHERE ID_aluno = {id_aluno}''')
    aluno = cursor.fetchone()

    if not aluno:
        print("Aluno não encontrado!")
        conexao.close()
        return
    else: 
        novo_nome = input("Digite o novo nome do aluno: ")
        novo_telefone = input("Digite o novo telefone: ")
        nova_tuma = input("Digite a nova turma: ")
        nova_idade = int(input("Digite a nova idade: "))
        novo_cpf = input("Digite o novo cpf: ")
    
        comando = f'''UPDATE alunos SET nome = '{novo_nome}', cpf = '{novo_cpf}, telefone = {novo_telefone}, turma = {nova_tuma}, idade = {nova_idade}'''


        print("Dados do aluno alterado")
        cursor.execute(comando)
        conexao.commit()
        conexao.close()


def excluir():

    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

    cursor.execute(f"SELECT * FROM alunos WHERE id_aluno = {id_aluno}")
    
    print("Aluno excluido")
    conexao.commit()
    conexao.close()

def menu():
    while True:
        print("---SISTEMA DE ALUNO---")
        print("1- Cadastrar aluno")  
        print("2- listar aluno")  
        print("3- Atualizar aluno")
        print("4- Excluir aluno")
        print("5- Sair")

        opcao = input("Escolha uma das opções para ser feita: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao =="4":
            excluir()
        elif opcao == "5":
            print("Encerrando sistema!")
            return
        else:
            print("Opção invalida!")
menu()    