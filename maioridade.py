ano = int(input("Digite seu ano de nascimento: "))
idade = 2026 - ano

if idade > 18:
    print(f"Você já tem maioridade, sua idade é: {idade}")
else:
    print(f"Você ainda não tem maioridade, sua idade é: {idade}")    