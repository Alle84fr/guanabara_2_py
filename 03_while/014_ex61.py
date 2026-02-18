# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o primeiro termo, número: "))
razao = int(input("Qual a razão, o pulo do valor: "))
contador = 10
lista_v = [termo]

while contador != 1:
    termo += razao
    lista_v.append(termo)
    contador-=1
print(lista_v)