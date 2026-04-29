def avaliar_desempenho(notas):
    if notas >= 9:
        return "Exelente"
    elif notas >= 7:
        return "bom"
    elif notas > 5:
        return "regular"
    else:
        return "Insuficiente"
    
valor_das_notas = float(input("Digite uma nota de 0 a 10: ")) 
resultado = avaliar_desempenho(valor_das_notas)
print(f"O resultado é {resultado}")