valores = list()
lista1 = []
lista2 = []

while True:
    num = int(input('Digite o valor: '))
    valores.append(num)

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()[0]
    while continuar not in ['s', 'n', 'S', 'N']:
        continuar = input('Opção invalida! Deseja continuar? [S/N]')

    if continuar == "n":
        break

print("-=-"*30)

print(f'Lista dos numeros digitados: {valores}')

for valor in valores:
    if valor % 2 == 0:
        lista1.append(valor)
print(f"PAR: {lista1}")

for valor2 in valores:
    if valor2 % 2 != 0:
        lista2.append(valor2)
print(f"ÍMPAR: {lista2}")