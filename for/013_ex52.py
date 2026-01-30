# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("valor: "))
total = 0

if num == 1 or (num>2 and num%2==0) or (num%5==0): print(f"{num} não é primo")
else: print(f"{num} é primo")

# me perdi nas regras
# professor

for c in range(1,num +1):
     if num % c == 0:
         print
