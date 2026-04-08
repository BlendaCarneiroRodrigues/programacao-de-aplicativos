valor = float(input("Digite qual foi o valor da compra R$: "))

if valor > 100.00:
    desconto = valor * 0.10
    final = valor - desconto
    print(f"A compra teve um desconto: R${final}")
else:
    print(f"Valor da sua compra: R${valor}")

