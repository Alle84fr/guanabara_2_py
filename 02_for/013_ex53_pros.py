frase = input("\nfrase: ")

# separa em lista
palavras = frase.split()
print(palavras)

# subtitui espaço entre as palavras
junto = "".join(palavras)
print(junto)

#inverter
inverso = ""

#(ultima letra- como inicia no 0, mas ao voltar inicia no 1, então a posição que seria 1 é 0, tira um| o comprimento é de 0 a 5, por exemplo, na volta é de 1 a 6, então tira 1 | último -1 é para mostrar que é de trás para frente)
for letra in range(len(junto)-1, -1, -1):
    print(junto[letra])
    inverso += junto[letra]

if inverso == junto:print("é pal")
else: print("Não é")

# _____________________________

# outra forma

pal = input("Pal: ")

separa = pal.split()
junta = "".join(separa)

inverte = junta[::-1]

if inverte == junta: print("é")
else: print("Não é")

# no meu coloquei lista para poder usar o for, mas tinha pensando em apenas inverter e comparar