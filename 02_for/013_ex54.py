#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

tem = 0
n_tem = 0
hoje = date.today().year

for i in range(7):
    ano = int(input("\n Ano: "))
    idade = hoje - ano
    if idade >= 18: tem += 1
    else:n_tem += 1
print(f"""Tem {tem} maioridade
Não tem {n_tem} maioridade""")