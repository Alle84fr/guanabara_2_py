# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

inte = int (input("n interiro: "))
base = int(input("base 2, base 8 ou base 16: "))
i = inte//base
b = inte%base
l = [b]
print(f"\033[96m lista {l} \033[m")
print(f"\033[96m resultado {i} \033[m")
print(f"\033[96m resto {b} \033[m")

if base == 2:
   while i != 0:
        print(f"\033[97m lista {l} \033[m")
        print(f"\033[97m resultado {i} \033[m")
        print(f"\033[97m resto {b} \033[m")
        b = i%base
        l.append(b)
        i = i//base
       
        print(f"\033[95m lista {l} \033[m")
        print(f"\033[95m resultado {i} \033[m")
        print(f"\033[95m resto {b} \033[m")

#__________________ !! ATENÇÃO !!__________________#

# ESTAVA 1° CALCULANDO O QUOCINETE, NO WHILE E DEPOIS PEGANDO O RESTO 
# PORÉM O CORRETO É PEGAR O RESTO E DEPOIS CALCULAR A DIVISÃO

# ESTAVA ASSIM

# if base == 2:
#    while i != 0:
#         print(f"\033[97m lista {l} \033[m")
#         print(f"\033[97m resultado {i} \033[m")
#         print(f"\033[97m resto {b} \033[m")
#         i = i//base
#         b = i%base
#         l.append(b)
       
#         print(f"\033[95m lista {l} \033[m")
#         print(f"\033[95m resultado {i} \033[m")
#         print(f"\033[95m resto {b} \033[m")

#mesmo assim deu erro