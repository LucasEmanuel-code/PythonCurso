'''matriz = [[],[],[]]

print('Digite os numeros da matriz 3x3: ')
for c in range(3):
    for j in range(3):
        num = int(input(''))
        matriz[c].append(num)

print('\nMatriz formada:')
for linha in matriz:
    print(linha)'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range (3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor: '))
print('--'*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
