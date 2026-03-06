numero_total_de_garrafas = int(input("digite o numero de garrafas que ja passaram pela estera hoje: "))

if numero_total_de_garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar a máquina imediatamente.")
    print("QUALIDADE: Retirar amostra para teste.")

elif numero_total_de_garrafas % 100 == 0:
    print("QUALIDADE: Retirar amostra para teste.")
