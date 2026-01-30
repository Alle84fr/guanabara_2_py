#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for n in range(1,51):
    if n%2 == 0:
        print(n)

#ou

for n in range(1,51):
    if n%2 == 0:
        print(n, end=" ")
# como no final coloquei que não pula linha, ao ir para o próximo laço, o resultado vem na mesma linhas, então coloquei pular linhas
print("\n")

#ou

lista = []

for l in range(1,51):
    if l%2==0:lista.append(l)
print(lista)

# professor
for n in range(2,51, 2):
    print(n, end=" ")

