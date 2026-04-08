numero = float(input("Digite um número para saber se ele é positivo ou negativo: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número {numero} é neutro")