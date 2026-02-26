nivel = int(input("digite o nivel do personagem: "))
esferas = int(input("digite a quantidade de esferas coletadas pelo personagem: "))

if nivel >= 20 and esferas >= 50:
    print("Habilidade Super Salto desbloqueada.")
elif nivel < 20 and esferas < 50:
    print("abilidade não desbloqueada")     
