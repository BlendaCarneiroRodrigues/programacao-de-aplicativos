senha = input("digite a senha: ")
tentativa = int(input("digite o numero de tentativas: "))
token = input("digite se você tem token (s/N): ")

if (senha == "adimin123" and tentativa % 3 == 0) or (token == "s"):
    print(f"Tentativa n°{tentativa}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa n°{tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")