nome = input("digite seu nome: ")
altura = float(input("digite sua altura: "))

if altura < 1.50:
    print("desculpe, você não tem altura minima", nome)
elif altura >= 1.50:
    print("acesso liberado! divirta-se na queda livre", nome)
