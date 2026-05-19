import json

with open("notas.json", 'w'):
    notas = {"matematica":8.5, "portugues":9.0}

with open('notas.json', 'r') as arquivo:
    soma = notas['matematica'] + notas['portugues']
    print(f"A soma das notas é: {soma}")