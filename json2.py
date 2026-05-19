import json

notas = {
    "matematica":8.5,
    "portugues": 9.0,
    "soma": 0
}


matematica = notas["matematica"]
portugues = notas["portugues"]


soma_devalor = matematica + portugues
notas["soma"] = soma_devalor

with open('notas.json','a') as arquivo:
    json.dump(notas, arquivo, ensure_ascii=False)

print("notas carregadas : ")
print(f"metmatica: {matematica}")
print(f"portugues : {portugues}")
print(f"soma das notas : {soma_devalor}")
