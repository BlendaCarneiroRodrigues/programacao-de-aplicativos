numeros = [1, 5, 8, 12, 15, 22, 7, 9, 30, 4]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)    
print(f"numeros pares: {pares}")  
print(f"numeros impares: {impares}")      