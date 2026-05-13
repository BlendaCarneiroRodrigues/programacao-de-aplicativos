open("alunos.txt", 'w').close()

def criar():
    nome = input("Nome do aluno: ")
    with open("alunos.txt", 'a') as f:
        f.write(nome + '\n')
    print("Aluno cadastrado!")


def ler():
    with open("alunos.txt", 'r') as f:
        alunos = f.readline()

        i = 0 
        for aluno in alunos:
            print(f"{i} - {aluno.strip()}")
            i += 1


def atualizar():
    ler()
    idx = int(input("Digite o ID do aluno que deseja alterar: "))
    nome_novo = input("Novo nome: ")

    with open("alunos.txt", 'r') as f:
        linhas = f.readline()

    linhas[idx] = nome_novo + '\n' 

    with open("alunos.txt", 'w') as f:
        f.writelines(linhas)
    print("Aluno auturizado")

def deletar():
    ler()
    idx = int(input("Digite o ID do aluno que deseja excluir: "))

    with open('alunos.txt', 'r') as f:
        linhas = f.readlines()

    del linhas[idx] 

    with open('alunos.txt', 'w') as f:
        f.writelines(linhas)
    print("Aluno removido!")


    while True:
        print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")   
        opcao = input("Escolha: ")


        if opcao == '1': criar()
        elif opcao == '2': ler()             
        elif opcao == '3': atualizar()
        elif opcao == '4': deletar()