saldo_inicial = 1000.00

print("1- deposito")
print("2- saque")
print("3- extrato")
menu = int(input("escolha uma das opções: "))

if menu == 1:
    valor = float(input("digite o valor para o depósito: "))
    if valor > 0:
        saldo_inicial = saldo_inicial + valor
        print("depósito realizado com sucasso!")
    else:
        print("valor invalidado para deposito.")

    print(f"saldo atual: {saldo_inicial}")

elif menu == 2:
    valor = float(input("digite o valor do saque: "))   

    if valor > 0 and (valor <= saldo_inicial or valor == 100):
        saldo_inicial = saldo_inicial - valor
        print("saque realizado com sucesso!")
    else:
        print("saque não altorizado.") 

    print(f"saldo atual: {saldo_inicial}")   
elif menu == 3:
    print(f"saldo atual: {saldo_inicial}")     

else:
    print("operaçao invalida!")
