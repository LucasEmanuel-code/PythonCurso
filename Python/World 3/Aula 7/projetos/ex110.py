def resumo(n, formatado=False):
    precos = 'Resumo dos Preços'
    tam = len(precos)+4
    print('-'*tam)
    print(f'  {precos}')
    print('-'*tam)

    n2 = n * 0.10
    aumento = n2 + n
    dobro = n *2
    metade = n // 2
    n3 = n * 0.10
    diminui = n - n3

    if formatado:
        aumento = f"R${aumento:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        dobro = f"R${dobro:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        metade = f"R${metade:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        diminui = f"R${diminui:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    print(f'Aumento de 10% {aumento}')
    print(f'Dobro: {dobro}')
    print(f'Metade: {metade}')
    print(f'Redução de 13%: {diminui} ')

    return aumento, dobro, metade, diminui
