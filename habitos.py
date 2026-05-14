open("habitos.txt", 'w').close()

def cria():
    habitos = input("Digite o hábito que deseja adicionar a lista: ")
    with open("habitos.txt", 'a') as h:
        h.write(habitos + '\n')
    print("Hábito adicionado na lista!")

def ler():
    with open("habitos.txt", 'r') as h:
        habitos = h.readlines()
        i = 0
        for habito in habitos:
            print(f"{i} - {habito.split()}")
            i += 1

def editar():
    ler()
    editar_destino = int(input("Digite o ID do hábito que deseja editar: "))
    novo_habito = input("Novo hábito: ")

    with open("habitos.txt ", 'r') as h:
        linhas = h.readlines()
    linhas[editar_destino] = novo_habito + '\n'

    with open("habitos.txt", 'w') as h:
        h.writelines(linhas)   
    print("Hábito editado!")    

def excluir():
    ler()
    excluir_habito = int(input("Digite o ID do hábito que deseja excluir: "))

    with open("habitos.txt", 'r') as h:
        linhas = h.readlines()

    del linhas[excluir_habito]

    with open("habitos.txt", 'w') as h:
        h.writelines(linhas)
    print("Hábito excluido!")

while True:
    print("\n---MEUS HÁBITOS---")
    print("\n1- Cadastrar hábito")
    print("\n2- Ver todos os hábitos") 
    print("\n3- Editar hábitos") 
    print("\n4- Excluir hábito")      
    opcao = input("Escolha: ")    

    if opcao == '1': cria()
    elif opcao == '2': ler()
    elif opcao == '3': editar()
    elif opcao == '4': excluir()