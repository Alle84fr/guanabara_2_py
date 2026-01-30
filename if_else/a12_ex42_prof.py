# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

a, b, c = map(int, input("lados: ").split())

if a < b + c and a > b + c and c < a + b:
    print("Pode formar um triãngulo")
    if a == b == c: print("Equilátero")
    elif a != b != c: print("Escaleno")
    else: print("Isósceles")
else:print("não forma triãngulo")