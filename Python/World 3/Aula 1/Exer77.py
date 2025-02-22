tupla = ('Marcenaria', 'Abacaxi', 'Suco',
         'Pizza', 'Olho', 'Cachorro',
         'Mamao', 'Macarrao', 'Python')

vogais = 'aeiouAEIOU'

for palavra in tupla:
    print(f'\nVogais em {palavra.upper()}: ', end='')
    for vogal in palavra:
        if vogal.lower() in vogais:
            print(vogal, end=' ')
