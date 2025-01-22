print("Qual o valor do produto? ")

produto = float(input("R$ "))

print("Escolha um valor de pagamento \n"
      "[1] dinheiro ou cheque\n"
      "[2] cartão\n"
      "[3] 2x cartão\n"
      "[4] 3x ou mais no cartão\n")
escolha = int(input(""))

juros = 20

if escolha == 1:
    e1 = produto * 0.90
    print(f"Em dinheiro ou cheque com 10% de desconto, fica {e1}R$")
elif escolha == 2:
    e2 = produto * 0.95
    print(f"No cartão com 5% de desconfo, fica {e2}R$ ")
elif escolha == 3:
    e3 = produto/2
    print(f"No cartão com 2x parcelando, fica {e3}R$")
elif escolha == 4:
    print("Digite o número de parcelas: ")
    parcelas = int(input(""))
    if parcelas >= 3:
        valor = produto * (1 + juros / 100)
        e4 = valor/parcelas
        print(f"No cartão com 3x ou mais parcelando, fica {e4}R$")
    else:
        print("Número de parcelas invalido, 3x ou mais")
else:
    print("Escolha apenas uma das 4 opções acima ")
