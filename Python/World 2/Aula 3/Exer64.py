print("Digite um número: ")

soma = 0
numero = 0

while numero != 999:
    numero = int(input(""))
    if numero != 999:
        soma += numero

print("Número 999 digitado. Programa encerrado.")
print(f"A soma dos números é: {soma}")