num = int(input("n°: "))

tot = 0

# ex: num = 9
# for vai de 1 a 9
# O valor será divido por 1, 2 ... até 9
# se o restor de 9 % c for == 0, então tot recebe 1 e cada rodada que entrar em if soma um
# se o resto for != 0 não conta tot (total)
# saindo do for
# se tot for 2 (1 e ele mesmo) é primo
# se for maior ou menor (aqui entra 1) não é primo
for c in range(1, num + 1):
    if num % c == 0:
        #todo resultado vindo deste if terá sua escrita amarela ([33m])
        print("\033[33m", end='')
        tot += 1
    else:
         #todo resultado vindo deste else terá sua escrita vermelha ([31m])
        print("\033[31m", end='')
    print(f"{c} ", end="")
print("\n\033[m0 número {c} foi divisível por {tot} vezes")
if tot == 2: print("e por isso ele é primo")
else: print("E por isso ele não é primo")