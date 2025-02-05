NBA = ('Cavaliers', 'Celtics', 'Knicks', 'Pacers',
       'Bucks', 'Heat', 'Pistons', 'Magic', 'Hawks',
       'Bulls', '76ers', 'Raptors', 'Nets', 'Hornets',
       'Wizards')

print(f"Times da NBA:")
print(f'{NBA}\n')

print(f'Na zona de Playoffs estão: ')
print( f'{NBA[:8]} \n')

print(f'Times que estão fora dos Playoffs: ')
print(f'{NBA[-4:]} \n')

NBA_ordenado = sorted(NBA)
print(f'Times em ordem alfabética: ')
print(f'{NBA_ordenado} \n')

print(f'Miami Heat está na posição:')
print(NBA.index('Heat'))
