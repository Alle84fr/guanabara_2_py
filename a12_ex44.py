#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valor = float(input("Valor: "))

tipo = input("Dinheiro, Cheque, Avista, Cartão 2x ou Mais X: ").lower()

match tipo:
    case "dinheiro":
        print(f"R$ {valor - (valor*0.10)}")
    case "cheque":
        print(f"R$ {valor - (valor*0.10)}")
    case "avista":
        print(f"R$ {valor - (valor*0.05)}")
    case "cartão 2x":
        print(f"2 Parcelas de R$ {(valor/2):.2f}, total de R${valor*2}")
    case "mais x":
        q = int(input("Quantas X: "))
        valor = valor + (valor*0.20)
        print(f"{q} parcelas de R$ {(valor/q):.2f}, toral de R${valor}")