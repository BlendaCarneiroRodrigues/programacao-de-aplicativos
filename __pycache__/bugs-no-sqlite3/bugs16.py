def menu():
    while True:
        print("1. Cdastrar Aluno")
        print("2. Sair")
        opcao = input("escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do programa.")

            break   

# o laço while não estáva sendo encerrado com o pass que está no final. (COREÇÃO: trocar o pass pelo break)