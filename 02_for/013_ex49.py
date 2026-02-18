#  Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

valor = int(input("qual tabuada vc quer? "))

for v in range(1,11):
    print(f"{valor} * {v} = {valor*v}")