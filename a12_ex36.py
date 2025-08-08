# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Valor da casa: "))
salar = float(input("Salário líquido: "))
anos = int(input("Quantidade de anos: "))

#Ler com atenção ele pediu anos, e parcelas saõ mensais, quase errei
parcela = anos*12
prest_men_div = valor/parcela
porc_30 = salar*0.3

if prest_men_div <= porc_30: print("Aprovado")
else:print("Reprovado")

#  |_____________________|  CORREÇÃO DO PROF  |___________________|


casa = float(input("Valor da casa: "))
salario = float(input("Salário líquido: "))
anos = int(input("Quantidade de anos: "))

#juntou em uma única variáel
prestacao = casa/(anos*12)

#porcentagem 30% de 100%
minino = salar*30/100

print(f"Para pagar um casa de R${casa} em {anos}\n Deve ter pretação de R${prestacao:.2f}")
if prestacao <= minino: print("Aprovado")
else:print("Reprovado")

#        OBS
# ao digitar no consele pode por valor assim, para nãos e perder
#1_000_000.00