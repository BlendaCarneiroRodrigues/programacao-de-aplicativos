nota = float(input("digite a nota do aluno: "))
presenca = int(input("digite a presença do aluno: "))

if nota >= 7.0 and presenca >= 75.0: 
    print("Parabéns! Você foi aprovado.")
elif nota < 7.0 and presenca < 75.0:
    print("Reprovado. Verifique sua nota e presença.")
    