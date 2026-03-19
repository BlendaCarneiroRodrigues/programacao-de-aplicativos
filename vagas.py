vagas = ["Livre","Ocupado","Livre","Ocupado"]
digite_vagas = int(input("Digite um numero de 0 a 3: "))
if digite_vagas >= 0 and digite_vagas <= 3:
    if digite_vagas % 2 == 0 and vagas == "Livre":
        print(f"Vaga {digite_vagas}")    
else:
    print(f"Vagas {digite_vagas} indisponivel ou fora das regras")    