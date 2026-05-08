def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):

    total = valor_base + (valor_base * imposto_percentual / 100)
    total -= cupom_desconto

    if total < 0:
        total = 0

    return total

valor_base = float(input("Digite o valor base do produto: R$ "))
imposto_percentual = float(input("Digite o percentual de imposto: "))
cupom_desconto = float(input("Digite o valor do cupom de desconto: R$ "))

preco_final = calcular_preco_final(
    valor_base,
    imposto_percentual,
    cupom_desconto
)
print(f"Preço final do produto: R$ {preco_final:.2f}")