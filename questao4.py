def esta_na_lista(lista_nome, busca):
    for nome in lista_nome:
        if nome == busca:
            return "Encontrado!"
    return "Não encontrado!"
frutas = ["maçã", "banana", "uva", "laranja", "manga"]
brucas1 = input("digite o nome de uma fruta para busca: ")
resultado = esta_na_lista(frutas, brucas1)
print(f"resultado da busca: {resultado}")