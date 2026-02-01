# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []

# no for o i, que é uma variável, será usado apenas na conategm interna, então, para mostrar que ele não é importante no retorno de valores, pode por underscore
# mas se fizer - for i in range(), não estará errado

for _ in range(5):
    peso = float(input("peso: "))
    lista.append(peso)
    #print(lista, end=" -")
print(f"\nO mais pesado da lista é {max(lista)}")
print(f"O menos pesado da lista é {min(lista)}\n")