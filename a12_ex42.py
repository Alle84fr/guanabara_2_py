# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes


a, b, c = map(int, input("lados: ").split())

#verificar se é ou não retãngulo
if a < b + c and b < a + c and c < a + b:
    if a == b == c: print("EQUILÁTERO: todos os lados iguais")
    elif a ==b or a == c or c == b: print("ISÓSCELES: dois lados iguais, um diferente")
    else: print("ESCALENO: todos os lados diferentes")
else: print("não é triãngulo")