vida_inicial = 1000
def sofre_dano(vida_inicial, valor_dano):
    
    while vida_inicial > 0:
        if valor_dano > valor_dano:
            return "Dano Critico, Game Over!"
        vida_inicial -= valor_dano
        print(f"A vida do personagem apos dano é {vida_inicial}")
        valor_dano = float(input("Digite o valor do dano causado no personagem: "))
    return "Game Over!"
valor_dano =  float(input("Digite o valor do dano causado no personagem: "))
mensagem = sofre_dano(vida_inicial, valor_dano)
print(mensagem)