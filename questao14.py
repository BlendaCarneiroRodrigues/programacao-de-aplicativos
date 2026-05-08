def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    return (nota_teste > 80 and anos_xp > 2) or possui_certificacao

nota_teste = float(input("Digite a nota do teste: "))
anos_xp = int(input("Digite os anos de experiência: "))

certificacao = input("Possui certificação? (s/n): ").lower()
possui_certificacao = certificacao == "s"
if verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    print("Contratar")
else:
    print("Descartar")