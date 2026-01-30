# iteração/ laços/ repetição/ estrutura de controle

# algoritmo = passo a passo para resolver algo

#laço com variável de controle - for

#vai de 1 a 9, pois o último valor não entra, se quisesse de 1 a 10 pode fazer de 1,10+1 ou 1,11
#10,0,-1 -> do 10 a 1
for c in range(10,0,-1):
    print(c)

s = 0

for i in range(0,3):
    n = int(input(f"Valor {i}: "))
    s += n
print(f"soma {s}")