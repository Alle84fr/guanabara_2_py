# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

flag =(input("Digite f para feminino ou m para masculino: ")).lower()

while flag != "m" and flag != "f":
    print("Valor incorreto")
    flag =(input("Digite f para feminino ou m para masculino: ")).lower()

print(f"Você é dos exo {flag}")

#__________________________________________________________________________________________________
#                         professor

#lembrando que strip tira espaços das pontas
#da palavra escrita em maiúscula [0] diz que pegará apenas a 1° letra
flag =(input("Digite apenas f para feminino ou m para masculino: ")).strip().upper()[0]

while flag not in "MF":
    flag =(input("Digite apenas f para feminino ou m para masculino: ")).strip().upper()[0]
print(f"{flag} registrado com sucesso")