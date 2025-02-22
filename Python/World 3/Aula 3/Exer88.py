'''from random import sample

print(10*' ','MEGA SENA')
print('___'*11)

print('Quantos jogos quer que eu sorteie?')
quantos = int(input(''))

for i in range(quantos):
    numeros = sorted(sample(range(1, 61),6))
    print(f'Jogo {i + 1}: {numeros}')'''

from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
         num = randint(1, 60)
         if num not in lista:
             lista.append(num)
             cont += 1
         if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*3, f'Sorteando {quant} Jogos', '-'*3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')