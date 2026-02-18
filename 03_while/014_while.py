
#while - enquanto true - sabe ou não sabe o limite

for c in range(1,10):
    print(c)

print("_"*25, "\n")

c = 1

while c < 10:
    print(c)
    c += 1
print("fim")

n = 1
while n!=0:
    n = int(input("Digite 0 para sair, ou qualquer outro inteiro para continuar: "))
    print("flag é 0, ponto de parada")
print("_"*25, "\n")

r = "S"

while r == "S":
    n = int(input("Digite um valor inteiro: "))
    r = input("Digite s para seguir ou n para não seguir: ").upper()
print("fim")

n = 1

par = impar = 0
list_par = []
list_impar = []

while n!=0:
    n = int(input("Digite um n°: "))
    if n != 0:
        if n%2 == 0:
            par += 1
            list_par.append(n)
        else: 
            impar += 1
            list_impar.append(n)

print(f"Foras {par} n°s pares e {impar} n°s impares")
print(f"lista par {list_par}")
print(f"lista impar {list_impar}")
print("_"*25, "\n")