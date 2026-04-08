nomes = ["Alice", "Gustao", "Maria", "Lucas"]
antigo = input("Qual nome você quer mudar da lista? ")
novo = input("Qual é o novo nome? ")

for i in range(len(nomes)):
    if nomes[antigo] == nomes:
        nomes[novo] = nomes

print("Lista atualizada:", nomes)

