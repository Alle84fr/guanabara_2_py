#  Crie um programa que faça o computador jogar Jokenpô com você.

import random

print("\n\33[0;30;106m 😃  Jooooqueeempô! 😒                          \033[m\n")
print("\33[1;91;103m 🫵  Atenção às regras: 🧐                       \033[m\n")
print("\33[0;30;107m 🤜  Mão fechada é pedra 🪨                      \033[m")
print("\33[0;30;107m Pedra quebra tesoura                           \033[m")
print("\33[0;30;107m 🖐  Mão aberta é papel 📜                       \033[m")
print("\33[0;30;107m Papel embrulha pedra                           \033[m")
print("\33[0;30;107m ✌  Dedo indicador e médio esticado é tesoura   \033[m")
print("\33[0;30;107m Tesoura corta papel ✂                          \033[m\n")
print("\33[0;30;106m Digite S para sair                             \033[m\n")

start = input("Digite C para comer a jogar ou s para sair: ").lower()
ganhou = 0
empatou = 0
perdeu = 0


if start == "c":
    
    name = input(" Digite como quer ser chamada/o: ").title()
    
    lista = ("pedra","papel", "tesoura") 
    
    while True:
        
        jogador = input("\nPedra 🤜 papel 🖐 ou tesoura ✌ ? ")
        
        if jogador not in lista: 
            print("Eitaaaaa escolha entre pedra, papel ou tesoura: ")
            continue

        computador = random.choice(lista)
        
        if (
            (jogador == "pedra" and computador == "tesoura") or (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra")):
            ganhou += 1
        
        elif jogador == computador: empatou +=1
        
        else: perdeu += 1
        
        emojis = {
            "pedra": "🤜",
            "papel": "🖐",
            "tesoura": "✌"
            }
        
        print(f"{name} jogou {emojis[jogador]} X Compuador jogou {emojis[computador]}")
        print(f"{name} ganhou {ganhou}, empatou {empatou} e perdeu {perdeu}")
        stop = input("\nDigite S para parar sair ou c para continuar: ").lower()
        if stop == "s": break
        

print("\n👾  Obrigada por jogar comigo  🤖 \n")