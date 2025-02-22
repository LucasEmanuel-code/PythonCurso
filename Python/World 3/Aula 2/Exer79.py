valores = list()

valores.sort()

while True:
    num = int(input('Digite o valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Este valor {num} já foi adicionado')

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()[0]

    if continuar == "n":
        print('='*40)
        print(f'Valores adicionados: {valores}')
        break


