import sqlite3

def criar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS professores (id_professor integer primary key autoincrement,
                    nome_completo_professor text not null,
                    materia_professor text,
                    idade_professor integer,
                    cpf_professor text unique not null,
                    salario_professor REAL,
                    nome_escola text not null
                    )''')

    nome_completo = input("Digite o nome completo do professor: ")
    materia = input("Digite a matéria do professor: ")
    idade = int(input("Digite a idade do professor: "))
    cpf = input("Digite o cpf do professor: ")
    salario = float(input("Digite o salário desse professor:R$: "))
    nome_da_escola = input("Digite o nome da escola que esse professor da aula: ")

    comando_inserir = f''' insert into professores(nome_completo_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_escola)
                        values ('{nome_completo}', '{materia}', '{idade}', '{cpf}', {salario}, '{nome_da_escola}')'''
    print("Professor cadastrado")
    cursor.execute(comando_inserir)
    conexao.commit()

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    if not professores:
        print("Nenhum professor encontrado")
    else:
        for professor in professores:
            print(f"id: {professor[0]} Nome: {professor[1]}, Matéria: {professor[2]}, Idade: {professor[3]}, CPF: {professor[4]}, Salário: {professor[5]}, Escola: {professor[6]}")    
    conexao.close()

def alterar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_busca = int(input("Digite o id que deseja alterar: "))
    cursor.execute(f'''SELECT * FROM professores WHERE id_professor = {id_busca}''')

    professor = cursor.fetchone()

    if not professor:
        print("Professor não encontrado!")
        conexao.close()
        return
    else:
        novo_nome = input("Digite o novo nome do professor: ")
        nova_materia = input("Digite a nova matéria: ")
        nova_idade = int(input("Digite a nova idade: "))
        novo_cpf = input("Digite o novo cpf: ")
        novo_salario = float(input("Digite o novo salário: "))
        novo_nome_escola = input("Digite o nome da nova escola: ")
        comando = f'''UPDATE professores SET nome_completo = '{novo_nome}', materia = '{nova_materia}', idade = {nova_idade}, cpf = '{novo_cpf}', salario = {novo_salario}, nome_da_escola = '{novo_nome_escola}' WHERE id = {id_busca}'''

        print("Professor alterado")
        cursor.execute(comando)
        conexao.commit()
        conexao.close()

def excluir():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    listar()
    id_professor = int(input("Digite o id do professor que deseja excluir: "))

    cursor.execute(f''' DELETE FROM professores WHERE id_professor = {id_professor}''')

    print("Professor excluido")
    conexao.commit()
    conexao.close()


def menu():
    while True:
        print("---SISTEMA DE PROFESSORES---")
        print("1- Cadastrar professor")  
        print("2- listar professores")  
        print("3- Alterar professor")
        print("4- Excluir professor")
        print("5- Sair")

        opcao = input("Escolha uma das opções para ser feita: ")

        if opcao == "1":
            criar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            alterar()
        elif opcao =="4":
            excluir()
        elif opcao == "5":
            print("Encerrando sistema!")
            return
        else:
            print("Opção invalida!")
menu()