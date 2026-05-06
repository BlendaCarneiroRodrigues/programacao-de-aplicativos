def calcular_area(largura, comprimento):
    multiplicar = largura * comprimento
    return multiplicar
tentativas = 0
while tentativas < 3:
        print(f"Terreno {tentativas + 1}")
        largura = float(input("Digite a largura do terreno: "))
        comprimento = float(input("Digite o comprimento do terreno: "))
    
        area = calcular_area(largura, comprimento)
        print(f"A área do terreno é: {area}")
        tentativas += 1