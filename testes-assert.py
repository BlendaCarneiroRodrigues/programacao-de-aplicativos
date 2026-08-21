# QUESTÃO 1: 

def dobrar(numero):
    return numero * 2

assert dobrar(3) == 6  # P - passa 
assert dobrar(0) == 1  # F - falha
assert dobrar(-2) == -4  # P - passa

# Registro:
# O segundo assert falhou.
# O resultado real de dobrar(0) é 0.



# QUESTÃO 2:

def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# Teste extra
assert situacao_aluno(7) == "Aprovado"

# 6 e 5.9 são casos de limite porque 6 é o valor
# em que a situação muda de Reprovado para Aprovado.
# 5.9 está imediatamente abaixo desse limite.



# QUESTÃO 3:

# Essa função contem um erro.
def calcular_desconto(preco, percentual):
    return preco - percentual

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 50) == 100
assert calcular_desconto(100, 0) == 100

# A função original está fazendo preco - percentual, mas o percentual precisa ser calculado sobre o preço.
# A forma certa de calcular é return preco - (preco * percentual / 100)

# A função correta é 
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 50) == 100
assert calcular_desconto(100, 0) == 100



# QUESTÃO 4:

def eh_par(numero):
    return numero % 2 == 0

# Esse teste falha.
assert eh_par(3) is True
# O problema está no teste, não na função.

# O resultado correto de eh_par(3) é False, portanto o teste correto é assert eh_par(3) is False



# QUESTÃO 5:

def frete_gratis(valor):
    return valor >= 200


assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True


def pode_votar(idade):
    return idade >= 16


assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True


def senha_valida(senha):
    return len(senha) >= 8


assert senha_valida("1234567") is False
assert senha_valida("12345678") is True
assert senha_valida("123456789") is True



# QUESTÃO 6:

def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas <= 10:
        return "Atenção"
    return "Reprovado por falta"


assert situacao_faltas(0) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(5) == "Atenção"
assert situacao_faltas(10) == "Atenção"
assert situacao_faltas(11) == "Reprovado por falta"



# QUESTÃO 7:

# Função escolhida: calcular_desconto
# Regra encontrada: o percentual deve ser calculado sobre o preço.

def calcular_desconto(preco, percentual):
    return preco - percentual


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 50) == 25

# A função acima apresenta erro porque está subtraindo diretamente o percentual.

def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 50) == 25



# QUESTÃO 8:

def pode_votar(idade):
    return idade >= 16


assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True

# Os testes 15 e 16 são importantes porque verificam exatamente o ponto em que a regra muda.



# QUESTÃO 9:

def buscar_nome(lista, nome):
    return nome in lista

def tem_senha_valida(senha):
    return len(senha) >= 8

# buscar_nome

assert buscar_nome(["João", "Maria"], "João") is True
assert buscar_nome(["João", "Maria"], "Pedro") is False
assert buscar_nome([], "João") is False

# tem_senha_valida

assert tem_senha_valida("1234567") is False
assert tem_senha_valida("12345678") is True
assert tem_senha_valida("123456789") is True

# Ao buscar um nome em uma lista vazia, o resultado é False, porque não existe nenhum nome na lista.



# QUESTÃO 10: 

def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    return "Quente"


assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14.99) == "Frio"
assert classificar_temperatura(15) == "Agradável"
assert classificar_temperatura(25) == "Agradável"
assert classificar_temperatura(25.01) == "Quente"

# Os testes de 15 e 25 são importantes porque são os limites definidos pela regra.