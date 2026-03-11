codigo_do_pacote = int(input("digite o codigo do pacote: "))
peso_do_pacote = float(input("digite o peso do pacote: "))

if peso_do_pacote > 50:
    print(f"pacote {codigo_do_pacote}: carga pessada!")

elif peso_do_pacote < 5 and codigo_do_pacote % 10 == 0:
    print(f"pacote {codigo_do_pacote}: entrega expressa")
else:
    print("seu pacote não entra nas condições.")    