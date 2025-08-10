# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#|____________________  Aprendendo o que são  __________________|

# sistema de numeração são formas de contar 

# 1 - binário = base 2 = compputador usa é de 0 e 1
# cada  dígito é um bit 

# 2 - Octal = base 8 = usa oito  dígitos, de 0 a 7
# computadores antigos usavam muito

# DECIMAL - base 10

# 3 - Hexadecimal = base 16 = muito comum em programação, de 0 a 9 e de A à F ( sendo A = 10 e F = 15)

#   PARA CONVERTER 
# divide pelo valor da base
# guarda o resto
# divide o resultado
# repete até o resulto for zero
# O RESULTADO SÃO OS VALORES DO RESTO, NA ORDEM DO ÚLTIMO AO PRIMEIRO (BAIXO PARA CIMA)

n_int = int(input("Digite valor inteiro: "))
sist_n =int(input("Digite 2 para conversão Binária, 8 para Octal ou 16 para Hexadecimal: "))

valor= [y]
print(f"\033[47m x = {x} \033[m ")
print(f"\033[47m y = {valor} \033[m ")

while sist_n not in {2,8,16}:
    print(f"o número {sist_n} não é valido")
    sist_n =int(input("Digite 2 para conversão Binária, 8 para Octal ou 16 para Hexadecimal"))
   
if sist_n == 2:
    while x != 0:
        print(f"\033[96m //x = {x} \033[m")
        y = x%sist_n
        valor.append(y)
        print(f"\033[94m {valor} \033[m")
        x //= 2
        lista = valor[::-1]
    print(f"O valor {sist_n} em Binário é {lista}")
elif sist_n == 8:
    while x != 0:
        print(f"\033[96m //x = {x} \033[m")
        valor.append(x%n_int)
        print(f"\033[94m {valor} \033[m")
        x //= 2
        lista = valor[::-1]
    print(f"O valor {sist_n} em Binário é {lista}")
else:
    while x != 0:
        print(f"\033[96m //x = {x} \033[m")
        valor.append(x%n_int)
        print(f"\033[94m {valor} \033[m")
        x //= 2
        lista = valor[::-1]
    print(f"O valor {sist_n} em Binário é {lista}")

conv = list(map(str, lista))
print(conv)

#errei