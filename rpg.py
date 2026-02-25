ataque = float(input("digite o poder de ataque do heroi: "))
defesa = float(input("digite o poder de defesa do vilão:"))

dano = ataque - defesa

if dano <= 0:
    print("o vilão bloqueou o ataque! dano:0")
elif dano > 0:
    print("ataque critico! você causou dano no vilão de:", dano)    