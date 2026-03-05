temperatura = float(input("digite a temperatura atual do ambiente: "))

if temperatura <= 30:
    print("clima estavel.")
elif temperatura > 30:
    print("Alerta de calor.") 
    umidade = float(input("digite a umidade do ambiente: ")) 
    if umidade < 40:
        print("Ação: ligar irrigação.")  
    else:
        print("Ação: ligar apenas ventiladores.")    