vida_personagem = 1.000
def sofre_dano(vida_aual, valor_dano): 
    nova_vida = vida_aual - valor_dano
    while vida_personagem > 0:
        dano = int(input("Digite o valor do dano causado no personagem: "))
if vida_personagem < 0:
      print("Game over!")