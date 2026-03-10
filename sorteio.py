id_do_usuario = int(input("digite o ID de usuario: "))
valor_da_compra = float(input("digite o valor da compra: "))

if id_do_usuario % 2 == 0 and valor_da_compra > 500.00:
    print(f"Parabens, usuário {id_do_usuario} você ganhou um cupom para sua compra de R$:{valor_da_compra}")
else:
    print(f"Obrigado pela compra usuário {id_do_usuario} continue acompanhando nossas promoções!")   