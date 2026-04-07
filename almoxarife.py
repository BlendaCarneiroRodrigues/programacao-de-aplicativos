itens = []

while True:
    print("\n1 - Adicionar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite um item: ")
        itens.append(item)
        print("Item adicionado com sucesso!")

    elif opcao == "2":
        if len(itens) == 0:
            print("Lista vazia.")
        else:
            print("Itens na lista:")
            for i, item in enumerate(itens, start=1):
                print(f"{i}. {item}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")