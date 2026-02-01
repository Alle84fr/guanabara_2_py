# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("valor: "))


if num == 1: 
    print("Não primo")

else:  
    for divisor in range(2,num):
        # o divisor irá iniciar em 2 e dividirá o valor num
        # se o resto de algum valor entre 2 e num -1 = a zero, para e retorna o resultado
        # valor não é dividido por ele mesmo, todos n°s são divisíveis por eles mesmo com o resto zero
        # queremos saber se é divisivel por outros valores
        if num%divisor == 0:
            print(f"O valor {num} não é primo")
            break
    else:
            print(f"O valor {num} é primo")

