km = int(input('\033[35mQuantidade de km percorridos:\033[m '))
dias = int(input('\033[33mQuantidade de dias que você ficou com o carro:\033[m '))
pagar = km * 60 + dias * 0.15
print('O total a pagar será de \033[32m{}\033[m'.format(pagar))