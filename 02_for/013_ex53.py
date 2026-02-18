# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Uma frase palíndroma é uma frase que pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda, ignorando espaços, acentos e pontuação.

# devo pegar um frase e ver seu tamanho(lenght)
# depois devo percorrer esta frase mas -1(fim para frente)
# por fim ver se elas são iguais ==

# .splt() separa frases
# list(palavra) separa string

frase = input("Frase: ")

# lowe() é para deixar tudo caixa baixa
# replace() é para tirar espaço e deixar sem espaço
frase = frase.lower().replace(" ","")

separa = list(frase)
print(separa)


lista = []
for i in separa:
    lista.append(i)
print(f"lista = {lista}")
    
volta = lista[::-1]
print(volta)

if separa == volta:
    print("É palíndromo")
else:
    print("Não é palíndromo")