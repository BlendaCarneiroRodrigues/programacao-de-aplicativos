numeros = [12, 45, 7, 89, 23, 56]
maior_valor = numeros[0]

for num in numeros:
    if num > maior_valor:
        maior_valor = num

print(f"O maior valor da lista: {maior_valor}")