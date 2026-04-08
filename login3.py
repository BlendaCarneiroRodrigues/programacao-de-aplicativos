senha = ["123"]
tentativas = 0
acertou = False 

while tentativas < 3 and not acertou:
    palpite = input("Tente adivinhar a senha: ")
    
    if palpite in senha:
        print("Acesso liberado!")
        acertou = True
    else:
        print("Senha incorreta")
    
    tentativas += 1
if not acertou:
    print("Suas tentativas acabaram.")
    print(f"A senha era: {senha}")

