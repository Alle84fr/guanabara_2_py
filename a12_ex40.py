# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

nota_1 = float(input("nota 1: "))
nota_2 = float(input("nota 2: "))

media = (nota_1+nota_2)/2

if media < 5:print("Reprovado")
elif 5 >= media <= 6.9:print("Recuperação")
else: print("Aprovado")