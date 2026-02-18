# Crie um programa que leia dois valores e mostre um menu na tela
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

menu = 0

while menu != 5:
    val_1, val_2 = map(int, input("dois valor: ").split())
    
    menu = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''))
    
    if menu == 1: print(f"{val_1} + {val_2} = {val_1+val_2}")
    elif menu == 2: print(f"{val_1} * {val_2} = {val_1*val_2}")
    elif menu == 3: 
        if val_1>val_2: print(f"{val_1} > {val_2} ")
        elif val_1<val_2: print(f"{val_1} < {val_2} ")
        else: print(f"{val_1} == {val_2} ")
    elif menu == 4: continue
    elif menu == 5: 
        print("Mas já?")
    else: 
        print("Valor errado")
        menu = int(input('''[ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa'''))

print("Obrigada por participar!")