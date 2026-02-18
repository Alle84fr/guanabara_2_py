somaIdade = 0
mediaIdade = 0
maioridade = 0
nomeVelho = ''
totalMulher = 0

for p in range(1,5):
    print(f"________ {p} PESSOA __________")
    
    nome = input("Nome: ").strip()
    sexo = input("Sexo [F/M]: ").strip()
    idade = int(input("idade: "))
    
    somaIdade += idade
    
    if p == 1 and sexo in "Mn":
        maioridade = idade
        nomeVelho = nome

    if sexo in "Mn" and idade > maioridade:
        maioridade = idade
        nomeVelho = nome
    
    if sexo in "Ff" and idade < 20:
        totalMulher += 1
    
mediaIdade = somaIdade / 4
print(f"A média de idade do grupo é de {mediaIdade}")
print(f"O homem mais velho tem {idade} e se chama {nome}")
print(f"são {totalMulher} mulheres com menos de 20 anos")