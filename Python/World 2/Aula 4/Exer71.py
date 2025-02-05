print("Banco do Brasil")

cedulas = [100, 50, 20, 10, 1]
n = 0

print("Que valor deseja sacar?")
valor = int(input("R$: "))

i = 0
while valor > 0:

    cedula = cedulas[i]
    i += 1

    if valor >= cedula:
        qnt = valor // cedula
        valor -= qnt * cedula
        print(f"Total de {qnt} cédulas de R$: {cedula}")

if valor > 0:
    print(f"O valor não pode ser sacado com as cédulas disponíveis.")
