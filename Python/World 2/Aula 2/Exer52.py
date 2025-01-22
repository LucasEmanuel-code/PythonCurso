amarelo = "\033[33m"
vermelho = "\033[31m"
parow = "\033[m"

print("Digite apenas um valor: ")
numero = int(input(""))
cont = 0

# Conta os divisores de 1 até o número
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1

# Verifica se o número é primo
if cont == 2:
    print(f"O número {amarelo}{numero}{parow} é primo.")
else:
    print(f"O número {vermelho}{numero}{parow} não é primo.")
