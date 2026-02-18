# não escrevi totalmente igual

from time import sleep

n1 = int(input("valor: "))
n2 = int(input("outro valor: "))

opcao = 0

while opcao != 5:
    
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input("Qual sua opção: "))
    
    if opcao == 1: print(n1+n2)
    elif opcao == 2: print(n1*n2)
    elif opcao == 3:
        if n1 > n2: print(n1)
        else: print(n2)
    elif opcao == 4:
        n1 = int(input("valor: "))
        n2 = int(input("outro valor: "))
    elif opcao == 5:print("finalizando")
    else: print("Opação iválida")
    
    print("_."*25)
    
    sleep(2)
    
print("fim do programa")