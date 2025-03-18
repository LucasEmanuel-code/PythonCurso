from random import randint
from time import sleep
nums = list()
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista:', end=' ')
    for num in lista:
        print(num, end=' ', flush=True)
        sleep(0.5)
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}')
sorteia(nums)
somaPar(nums)