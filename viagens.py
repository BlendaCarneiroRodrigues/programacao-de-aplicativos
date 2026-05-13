open ("viagens.txt", 'w').close()

def criar():
    destino = input("Digite sua sugestão de destino: ")
    with open("viagens.txt", 'a') as v:
        v.write(destino + '\n')
    print("Destino adicionado a lista!")

def ler():
    with open("viagens.txt", 'r') as v:
        viagem = v.readline()

        i = 0
        for viagens in viagem:
            print(f"{i} - {viagens.split()}")
            i += 1

def editar():
    ler()
    edita = int(input("Digite o ID do destino que deseja alterar: "))
    novo_destino = input("Novo destio: ")

    with open("viagens.txt", 'r') as v:
        linhas = v.readline()
    linhas[edita] = novo_destino + '\n'

    with open("viagens.txt", 'w') as v:
        v.writelines(linhas) 
    print("Destino editado!")


def excluir():
    ler()
    edita = int(input("Digite o ID do destino que quer deletar: "))

    with open("viagens.txt", 'r') as v:
        linhas = v.readlines()

    del linhas[edita] 

    with open('alunos.txt', 'w') as v:
        v.writelines(linhas)
    print("Destino removido!")

while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")   
    opcao = input("Escolha: ")

    if opcao == '1': criar()
    elif opcao == '2': ler()             
    elif opcao == '3': editar()
    elif opcao == '4': excluir()