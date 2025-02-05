numero = int(input("Digite um número: "))

posicao = ["Unidade", "Dezena", "Centena", "Milhar", "Dezena de Milhar", "Centena de Milhar", "Milhão"]
indice = 0
digitos = 0
temp = numero

while temp > 0:
    temp //= 10
    digitos += 1

print(f"O número {numero} possui {digitos} dígitos.")

while numero > 0 and indice < len(posicao):
    digito = numero % 10
    print(f"{posicao[indice]}: {digito}")
    numero //= 10
    indice += 1