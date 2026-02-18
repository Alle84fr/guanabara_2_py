from math import factorial

num = int(input("Numero: "))

fatorial = factorial(num)

print(f"Fatorial de {num} é {fatorial}" )

#_________________________________________________________________

#                             outra froma 

#_________________________________________________________________

contador = num
fator = 1

print(f"Calculando {num}! ", end="")
while contador > 0:
    print(f"{contador}", end="")
    print(f" X " if contador > 1 else " = ", end="")
    fator *= contador
    contador -= 1
print(f"{fator}", end="")
