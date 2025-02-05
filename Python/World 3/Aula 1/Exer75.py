numeros = []
for i in range(4):
    num = int(input(f'Digite o {i + 1} numero: '))
    numeros.append(num)

print("Tupla:", numeros[0], numeros[1], numeros[2], numeros[3] )

print(f"Quantas vezes apareceu o numero 9? {numeros.count(9)}")

if 3 in numeros:
    print(f"Em que posição aparece o numero 3? Posição: {numeros.index(3) + 1}")
else:
    print('Não encontrado')

print(f'Os numeros pares dentro da tupla são:')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')

