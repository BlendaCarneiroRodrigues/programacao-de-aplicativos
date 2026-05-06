def converter_km_para_ms(quilometros_por_hora):
    converter = quilometros_por_hora / 3.6
    return converter
velocidade = float(input("Digite a sua velocidade: "))

if velocidade > 80:
    velocidade_ms = converter_km_para_ms(velocidade)
    print(f"Velocidade em m/s {velocidade}")
    print("Reduza a velocidade!")
else:
    print("Velocidade dentro do limite")    