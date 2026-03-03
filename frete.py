valor_da_compra = float(input("dgite o valor da sua compra: "))
prime = input("digite se você é prime (S/N): ")

frete = 50.00

if valor_da_compra > 500.00 or (prime == "S" and valor_da_compra > 100.00):
    print("o seu frete é gratis ")
    frete = 0.0
    
frete_nao_gratis = valor_da_compra + frete    












