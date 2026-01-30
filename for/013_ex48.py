# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

som =0
cont = 0
#começa no 1 pula para 3,5,7,9...
for i in range(1,501, 2):
    if i%3==0:
        som += i
        cont += 1
        print(i)
print(som)
print(cont)
