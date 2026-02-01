#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

ida = 0
soma = 0
info = {}
mas = {}

for i in range(4):
    nome = input(f"{i}° nome: ")
    idade = int(input(f"{nome} tem a idade: "))
    sexo = input(f"{nome} opção sexual m, f, outra: ").lower()
    
    info[nome] = [idade,sexo]
    print(f"\033[33m {info.keys()}\033[m")
    # para acessar valores das chaves, lembrar que elas são listas, com índices numéricos
    print(f"\033[33m {info[nome][0]} \033[m\n")
    
    if sexo == "m":
        if i == 0 :
            ida = info[nome][0]
            name = info[nome]
        else:
            if ida < idade:
                name = info.keys()
                print(f"\033[34m {name} \033[m]")

    
    soma += info[nome][0]

   

    
# print(info)
print(f"média {soma/4}")

    # print(f"Mais velho é {velho[nome]}")