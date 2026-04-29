def senha_valida(senhas):
    return len(senhas) >= 6
while True:
    senha = input("Digite a senha para verificação: ")

    if senha_valida(senha):
        print("Senha cadastrada com sucesso!")
    else:
        print("Senha invalida para cadastro!")    