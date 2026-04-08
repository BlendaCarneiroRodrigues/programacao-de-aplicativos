produtos = []
saida = ""

while saida != "sair":
    saida = input("Digite um produto pra colocar no carrinho: ")
    if saida != "sair":
        produtos.append(saida)
print(f"Sua lista de produtos {produtos}")

