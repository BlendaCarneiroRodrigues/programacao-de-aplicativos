def analisar_vendas(nome, lista_vendas, meta_mensal):
    media = sum(lista_vendas) / len(lista_vendas)

    if media >= meta_mensal:
        resultado = "bateu"
    else:
        resultado = "não bateu"

    return f"O vendedor {nome} teve média de {media:.2f} e {resultado} a meta"

nome = "Carlos"
vendas = [1200, 1500, 1100, 1900]
meta = 1400

mensagem = analisar_vendas(nome, vendas, meta)

print(mensagem)