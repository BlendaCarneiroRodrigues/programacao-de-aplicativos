def somar_carrinho(precos):
    total = (precos)

    if total > 500:
        total *= 0.9

    return total

lista_compras = [120.50, 250.00, 180.75, 90.00]

valor_final = somar_carrinho(lista_compras)

print(f"Valor final a pagar: R$ {valor_final}")