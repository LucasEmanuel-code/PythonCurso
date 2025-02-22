valores = list()

while True:
    num = int(input('Digite o valor: '))
    valores.append(num)

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()[0]
    while continuar not in ['s', 'n', 'S', 'N']:
        continuar = input('Opção invalida! Deseja continuar? [S/N]')

    if continuar == "n":
        break

print('=' * 40)

if 5 in valores:
    print('O numero 5 está na lista')
else:
    print('O numero 5 não está na lista')

print(f'Numeros digitados: {len(valores)}')

valores.sort(reverse=True)
print(f'Valores em ordem decrescente: {valores}')



