import json

frase = input("Digite uma frase: ")
dicionario = {"mensagem": frase}

with open("teste.json", 'w') as teste:
    json.dump (dicionario, teste, ensure_ascii=False, indent=4)
    print("Arquivo teste.json criado com sucesso!")    
