# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

multipluicando = int(input("Digite um numero: "))
multiplicador = multipluicando-1
lista = [multipluicando, multiplicador]
conta = multipluicando * multiplicador

while multiplicador != 1:
    
    multiplicador -= 1
    #print(f"multiplicador = {multiplicador}")
    conta = conta * multiplicador
    #print(f"conta = {conta}")
    lista.append(multiplicador)
    #print(lista)

#função join é apenas para sting então deve converter inr para string
#função map mapeia cada elemento e aplica outra função em cada item

print(f"{' X '.join(map(str, lista))} = {conta}")