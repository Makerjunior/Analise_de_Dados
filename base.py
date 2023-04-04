print('Interpolação de strings')
nome = 'Junior Pereira'
# Modo 1 - usando formatadores de caracteres (igual na linguagem C) para imprimir variável e texto
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome))
# Modo 1 - usando formatadores de caracteres (igual na linguagem C) para imprimir variável e texto
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome))
# Modo 3 - usando strings formatadas
print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")

##########################################################################################################################

print('Operadores logicos')
# Qual o resultado armazendo na variável operacao_1: 25 ou 17?
operacao_1 = 2 + 3 * 5

# Qual o resultado armazendo na variável operacao_2: 25 ou 17?
operacao_2 = (2 + 3) * 5

# Qual o resultado armazendo na variável operacao_3: 4 ou 1?
operacao_3 = 4 / 2 ** 2

# Qual o resultado armazendo na variável operacao_4: 1 ou 5?
operacao_4 = 13 % 3 + 4

a = 2
b = 0.5
c = 1
# x = input("Digite o valor de x: ")
x = 3
x = float(x)  # aqui fazemos a conversão da string para o tipo numérico
y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")

print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")

#########################################################################################################################
print('Calculo de vanda de peças')

c = 200  # valor da constante

# mes = input("Digite o mês que deseja saber o resultado: ") # Função para captura o mês que o cliente digitar
mes = 6
mes = int(mes)  # Não esqueça de converter para numérico o valor captura pela função input()

r = c * mes  # Equação do primeiro grau, também chamada função do primeiro grau ou de função linear.

print(
    f"A quantidade de peças para o mês {mes} será {r}")  # Impressão do resultado usando string interpolada "f-strings" (PEP 498)

##############################################################################################################################

print('Calculo de numeros')

a = 5
b = 10

if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)

codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")

# qtde_faltas = int(input("Digite a quantidade de faltas: "))
# media_final = float(input("Digite a média final: "))
media_final = 3
qtde_faltas = 4
if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C)

numero = 1
while numero != 0:
    # numero = int(input("Digite um número: "))
    numero = 0
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

nome = "Guido"
for c in nome:
    print(c)

nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")

for x in range(5):
    print(x)

# Exemplo de uso do break
disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)

    # Exemplo de uso do continue
disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)

texto = """
A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado (BANIN, p. 45, 2018)."
"""
for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Vogal '{c}' encontrada, na posição {i}")
    else:
        continue

import datetime

agora = datetime.datetime.now()

hora_atual = agora.hour
minuto_atual = agora.minute
segundo_atual = agora.second
microsegundo_atual = agora.microsecond

hora_atual_str = agora.strftime('%H:%M:%S.%f')

print("Hora atual: ", hora_atual)
print("Minuto atual: ", minuto_atual)
print("Segundo atual: ", segundo_atual)
print("Microsegundo atual: ", microsegundo_atual)
print("Hora atual em string: ", hora_atual_str)

salario = 0
salario = 2000
# salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"O colaborador isento de imposto.")
    print(f"Salário a receber = {salario}")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$ 142,80 de imposto.")
    print(f"Salário a receber = {salario - 142.80}")
elif salario <= 3751.05:
    print(f"O colaborador deve pagar R$ 354,80 de imposto.")
    print(f"Salário a receber = {salario - 354.80}")
elif salario <= 4664.68:
    print(f"O colaborador deve pagar R$ 636,13 de imposto.")
    print(f"Salário a receber = {salario - 636.13}")
else:
    print(f"O colaborador deve pagar R$ 869,36 de imposto.")
    print(f"Salário a receber = {salario - 869.36}")


def calucular(*args):
    r = sum(args)
    for i in args:
        r += i
        return r
        print(r)


print(calucular(1, 4, 5))
x = calucular(1, 4, 5)
print(x)


#####################################################################################################
def calcular_desconto(valor, desconto=0):  # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto


valor1 = calcular_desconto(100)  # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25)  # Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")


######################################################################################################
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()


texto = converter_maiuscula(flag_maiuscula=True, texto="João")  # Passagem nominal de parâmetros
print(texto)


#######################################################################################################
def converter_minuscula(texto, flag_minuscula=True):  # O parâmetro flag_minuscula possui True como valor default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()


texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")

print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")


#####################################################################################################
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")


print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "João")

print("\nChamada 2")
imprimir_parametros(10, "São Paulo")


#####################################################################################################
def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")


print("\nChamada 1")
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")

print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)

##################################################################################################################
r = (lambda x: x + 1)(x=3)
print(r)
t = (lambda x, y: x + y)(x=3, y=2)
print(t)
somar = lambda x, y: x + y
g = somar(x=5, y=3)
print(g)


##################################################################################################################
def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
    v_bruto = valor_prod * qtde

    if desconto:
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif acrescimo:
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto

    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0


valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")

#####################################################################################################
"""
Essas linhas verificam se há um argumento nomeado 'desconto' ou 'acrescimo'
passado como um argumento nomeado adicional **kwargs para a função.
Se houver um 'desconto', a variável desconto será definida como o valor do argumento,
e o valor líquido será calculado subtraindo o desconto percentual do valor bruto. 
Se houver um 'acrescimo', a variável acrescimo será definida 
como o valor do argumento e o valor líquido será calculado adicionando o acréscimo percentual ao valor bruto.
Se não houver nenhum argumento de desconto ou acréscimo, o valor líquido será igual ao valor bruto.
"""


def calcular_valor(valor_prod, qtde, moeda="real", **kwargs):  # **kwargs permite a passagem de argumentos opcionais
    v_bruto = valor_prod * qtde

    if 'desconto' in kwargs:  # Verificando a passagem de possivél argumento
        desconto = kwargs['desconto']  # Instancia de variavel caso exista o argumento
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif 'acrescimo' in kwargs:
        acrescimo = kwargs['acrescimo']
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto

    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0


valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")