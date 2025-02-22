matriz = [[],[],[]]
somapar = 0
somacoluna = 0

print('Digite os numeros da matriz 3x3: ')
for c in range(3):
    for j in range(3):
        num = int(input(''))
        matriz[c].append(num)

        if num % 2 == 0:
            somapar += num

        if j == 2:
            somacoluna += num

segunda_linha_maior = max(matriz[1])
print('\nMatriz formada:')
for linha in matriz:
    print(linha)

print(f'\nSoma dos numeros pares: {somapar}')
print(f'Soma da 3 coluna: {somacoluna}')
print(f'o maior numero da 2 linha é: {segunda_linha_maior}')