lista = ["maçã", "banana", "laranja", "uva"]

while lista:
    print(f"Lista{lista} ")
    removido = lista.pop()  
    print("Removido:", removido)
print("Lista final:", lista)

