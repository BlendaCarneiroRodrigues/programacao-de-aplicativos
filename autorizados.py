autorizados = ["Alice", "Bob", "Carlos"]
nome = input("Digite o nome de um pesquisador: ")


if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso permitido! O pesquisador {nome} está na posição {indice}")

    remover = input("Você gostaria de remover esse pequisador da lista (s/n): ")   
    if remover == "s":
        autorizados.remove(nome) 
        print(f"lista atual {autorizados}")
    else:
        print("Saindo do programa...")
else:
    print(f"Acesso Negado! O Pesquisador {nome} não foi encontrado.")
    cadastrar = input("Você gostaria de cadastra esse pesquisador? (s/n): ")
    if cadastrar == "s":
        autorizados.append(nome)
        print("O pesquisador foi cadastrado.")
        print(f"Nova lista {autorizados}")
    else:
        print("Nem uma alteração foi feita")





    