from random import randint
from time import sleep
dici = dict()

for jogador in range(1, 5):
    dado = randint(1, 6)
    dici[f'Jogador {jogador}'] = dado
    print(f'Jogador {jogador} tirou {dado} no dado')
    sleep(1)
rank = sorted(dici.items(), key=lambda  x: x[1], reverse=True)

print('\n Ranking dos Jogadores')

for i, (jogador, result) in enumerate(rank, 1):
    print(f'{i}º lugar: {jogador} com {result} ')
    sleep(1)