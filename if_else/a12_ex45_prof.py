from random import randint
#biblioteca time para dar delay o jokempo
from time import sleep

itens = ("pedra", "papel", "tesoura")

#no meu escolho choice, que escolhe um elemento, não importamto qual
#randint escolhe entre os n° posto, apenas int
computador = randint(0,2)
print("""Suas ecolhas
[0] pedra
[1] papel
[2] tesoura""")

jogador = int(input("Qual é a sua jogada? "))

#delay de prints
print("Jooo")
sleep(1)
print("kennn")
sleep(1)
print("pooo")
sleep(1)

print("-="*11)
print("Jogador jogou {}".format(itens[jogador]))
print("-="*11)

# comptador jogou pedra
if computador == 0:
    if jogador == 0:print("empate")
    elif jogador == 1:print("jogador venceu")
    if jogador == 2:print("computador venceu")
# comptador jogou papel
if computador == 1:
    if jogador == 0:print("computador venceu")
    elif jogador == 1:print("empate")
    if jogador == 2:print("jogador venceu")
# comptador jogou tesoura
if computador == 2:
    if jogador == 0:print("jogador venceu")
    elif jogador == 1:print("computador venceu")
    if jogador == 2:print("empate")
        
