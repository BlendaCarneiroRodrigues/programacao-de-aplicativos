livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
escolha = input("Digite o livro que você deseja: ")

if escolha in livros_disponiveis:
    livros_disponiveis.remove(escolha)
    livros_emprestados.append(escolha)
    print(f"Empréstimo realizado com sucesso!")
    print(f"lista com livros emprestados: {livros_emprestados}")
else:
    print("Desculpe, este livro não está no acervo.")

devolucao = input("Digite o livro que você esta devolvendo: ")

if devolucao in livros_emprestados:
    livros_emprestados.remove(devolucao)
    livros_disponiveis.append(devolucao)
    print("Devolução feita.")
else:
    print("Este livro não consta como emprestado.")

del livros_disponiveis[0:2]
print(f"lista de livros disponiveis: {livros_disponiveis}")
print(f"lista de livros emprestados: {livros_emprestados}")       