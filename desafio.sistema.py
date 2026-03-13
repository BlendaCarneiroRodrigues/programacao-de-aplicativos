nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
telefone = int(input("digite seu numero: "))
carteira_de_motorista = input("Você tem carteira de motorista? (s/n): ")

if nome == "João" or "Thiago" or "Pedro" or "Matheus":
    print("Salvamento da lista cancelado")
elif telefone == 99999999:
    print("Telefone invalido")  