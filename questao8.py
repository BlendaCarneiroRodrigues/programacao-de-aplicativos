def contar_caracteres(palavras):
    while len(palavras) < 5:
        print("Palavra muito curta!")
        palavras = input("Digite uma palavra novamente: ")
    print("Palavra aceita!")

palavra_usuario = input("Digite uma palavra: ")
contar_caracteres(palavra_usuario)