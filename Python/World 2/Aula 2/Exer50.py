soma = 0
print("Digite 6 números inteiros:")

# Loop para obter 6 números do usuário
for _ in range(6):
    num = int(input("Número: "))
    if num % 2 == 0:
        soma += num
    else:  # Caso contrário, é ímpar
        print(f"O número {num} é ímpar e não será somado.")
# Exibe a soma dos números pares
print(f"A soma dos números pares é: {soma}")
