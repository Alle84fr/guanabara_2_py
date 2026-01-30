# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#meu
termo = int(input("Digite o primeiro termo, número: "))
razão = int(input("Qual a razão, o pulo do valor: "))

#não calculei o n-ésimo termo, aqui vai de por exemplo 1 a 13, printadndo só até 12, e não os 10 n°s existentes
for n in  range(termo, 11+termo, razão):#errei
    print(n)

#professor

decimo_fomula = termo + (10-1) * razão

for c in range(termo, decimo_fomula, razão):
    print(f"{c}")