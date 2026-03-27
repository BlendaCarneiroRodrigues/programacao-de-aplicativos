compra = []
item = ""
while item != "fim":
    item = input("Produto: ")
    if item != "fim":
        compra.append(item)
for produtos in compra:
    print(produtos)