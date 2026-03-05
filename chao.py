curso = input("O aluno concluiu o cuso de Segurança (s/n): ")

if curso == "n":
    print("Acesso negado: faça o treinamento primeiro.")
elif curso == "s":
    instrutor = input("O instrutor esta presente na sala? (s/n): ")
    if instrutor == "s":
        print("Acesso liberado: operação iniciada.") 
    else:
        print("Aguarde o instrutor para ligar a maquina.")       