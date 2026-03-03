media = float(input("digite a sua media: "))
renda = float(input("digite a sua renda: "))
escola = input("digite se você era de escola publica (S/N): ")

if media > 8.0 and (renda < 2.000 or escola == "S"):
    print("Ganhou a bolsa!")
else:
    print("Não atende os requisitos!")    
