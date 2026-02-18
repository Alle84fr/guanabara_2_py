from random import randint

computador= randint(0,10)
# ainda não acertou
acertou = False
palpite = 0

# enquanto não acertou - not false = true, enquanto verdade
while not acertou:
    jogador = int(input("digite valor de 0 a 10: "))
    
    if jogador == computador:
        #flag para sair é false, not true (do while) é false
        acertou = True

    else:
        if jogador < computador:print("O valor é maior")
        else:print("O valor é menor")
        
    palpite += 1
    
print("Acertou!!")
print(f"Palpitou {palpite} vezes")