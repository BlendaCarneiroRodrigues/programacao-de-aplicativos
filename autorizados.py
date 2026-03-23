autorizados = ["Alice", "Bob", "Carlos"]
nome = input("Digite o nome de um pesquisador: ")
indice =autorizados.index(autorizados)

if nome == autorizados:
    print(f"Acesso permitido! O pesquisador {nome} está na posição {indice}")

remover = input("Você gostaria de remover esse pequisador da lista (s/n): ")   
if remover == "s":
    autorizados.remove(nome) 
    