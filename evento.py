idade = int(input("digite sua idade: "))
saldo = float(input("digite o seu saldo: "))

if idade >= 18 and saldo >= 50.00:
    print("Acasso autorizado. Bem-vindo ao evento.")
elif idade < 18 and saldo < 50.00:
    print("Infelizmente você não cumpre os requisitos de entrada.")    