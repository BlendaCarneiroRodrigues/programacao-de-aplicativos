idade = int(input("digite a sua idade: "))
ingresso = input("digite se você tem ingresso (S/N) ")
lista = input("digite se você esta na lista (S/N) ")

if idade >= 18 and (ingresso == "S" or lista == "S"):
    print("seja bem vindo!")
else:
    print("você não tem acesso!")    
