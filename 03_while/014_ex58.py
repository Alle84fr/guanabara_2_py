# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

list_num = list(range(11))

chute = int(input("Qual n° entre 0 e 10 foi sorteado? "))
sair = "s"
sorteio = random.choice(list_num)
palpite = 0


while sorteio != chute:
    print(f"O valor {chute} não é o mesmo que o sorteado")
        
    sair = input("Se quiser sair digite s, se quiser continuar digite qualquer letra: ").strip().lower()[0]
    if sair == "s": break
        
    chute = int(input("Chute novamente n° entre 0 e 10 foi sorteado? "))
        
    palpite += 1

print("__"*25)
print(f"\nO valor {sorteio}")
print(f"Você chutou {palpite} x")
if sorteio == chute: print(f"Ebaaaa seu chute {chute} foi certeiro")
print(f"\nObrigada por jogar!")