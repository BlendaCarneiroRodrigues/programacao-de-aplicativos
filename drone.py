print("- Fase de Indentificação -")
codigo = int(input("digite o codigo do drone: "))
autorizacao = input("O drone possui autorização de Torre (s/n): ")

if codigo == 999 or autorizacao == "s":
    print("tudo certo: Iremos avançar para a anlise de pouso.")
    
    print("- Fase de analise de Voo -")
    bateria = float(input("digte o nivel de bateria do drone: ")) 
    clima = input("qual o clima no momento?: ") 
    velocidade_do_vento = float(input("digite a velocidade do vendo (km/h): ")) 

    if bateria < 10:
            print("EMERGENCIA: pouse imediatamente!")
    elif bateria >= 10 and clima == "ensolarado" and velocidade_do_vento < 30 or clima == "chuvoso" and velocidade_do_vento < 10:
            print("POUSO ALTORIZADO: inociando decida.")
    else:
            print("POUSO NEGADO: condições metereológicas perigosas. Aguarde em órbita")
else:
    print("ERRO 01: Drone não indentificado. retornando a base.")

