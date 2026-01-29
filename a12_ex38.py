# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# resolução do professor praticamente igual


def comparar(n1, n2):
    
    if n1 > n2: print("Primeiro valor maior")
    elif n1 < n2: print("Segundo valor maior")
    else: print("Não existe valor maior, os dois são iguais")
    
n_1 = int(input("Numero 1: "))
n_2 = int(input("Numero 2: "))

print(comparar(n_1, n_2))