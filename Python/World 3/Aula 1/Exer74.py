from random import randint

tupla = (0,1,2,3,4,5,6,7,8,9,10)

sorteado = [tupla[randint(0, len(tupla) -1)] for i in range(5)]

print(f'Os numeros sorteados foram: {sorteado}')

menor = min(sorteado)
maior = max(sorteado)

print(f'O maior numero foi:{maior}')
print(f'O menor numero foi: {menor}')

