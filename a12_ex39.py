#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Ano nascimento: "))
idade = 2026 - ano

if idade < 18: 
    falta = 18 - idade
    print(f"Ainda vai se alistar, faltam {falta} anos")
elif idade == 18: print("Deve se alistar")
else : 
    passou = idade - 18
    print(f"Já deveria ter se alistado, já passou {passou} anos")

