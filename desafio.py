nome = input("digite o seu nome: ")
valor_total_da_compra = float(input("digite o valor da compra: "))
frete = int(input("digite a distancia da entrega: ")) 
cupom_especial = input("Você possui cupom especial?(S/N):")
desconto = 0 



if valor_total_da_compra >= 1.000 and cupom_especial == "S":
   desconto = valor_total_da_compra * 0.20
   valor = valor_total_da_compra - desconto


elif valor_total_da_compra > 500.00 and cupom_especial =="S":
    desconto= valor_total_da_compra * 0.10
    valor = valor_total_da_compra - desconto 

if valor_total_da_compra >= 200.00 and frete >= 50:
        frete= 0 
        valor_final = valor + frete
else: 
     valor_final = valor + frete


print("seu nome é: ", nome)
print("o valor da sua compra é: ", valor_total_da_compra)
print("o valor total é: ", valor)
print("o valor final é: ", valor_final)








