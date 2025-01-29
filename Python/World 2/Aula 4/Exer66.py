print("Digite um número: ")

soma = 0
numero = 0
cont = 0

while True:
    numero = int(input(""))
    if numero == 999:
        break
    soma += numero
    cont += 1

print("Número 999 digitado. Programa encerrado.")
print(f"A soma dos valores {cont} é: {soma}")