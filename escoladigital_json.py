import json 

dados = {"cpf": cpf,
         "nomes": nome,
         "tlefones": telefone,
         "turmas": turma,
         "idades": idade
}

cpf = input("Digite o CPF do aluno: ")
nome = input("Digite o nome do aluno: ")
telefone = int(input("Digite o telefone do aluno: "))
turma = input("Digite a turma do aluno: ")
idade = int(input("Digite a idade do aluno: "))


with open("alunos.json", 'w') as alunos:
    json.dump(dados,alunos,)