tupla = ('Marcenaria', 'Abacaxi', 'Suco',
         'Pizza', 'Olho', 'Cachorro',
         'Mamao', 'Macarrao', 'Python')

vogais = 'aeiouAEIOU'

for palavra in tupla:

    vogais_palavra = [letra for letra in palavra if letra in vogais]

    print(f'Vogais em {palavra.upper()}:', end=" ")
    for vogal in vogais_palavra:
        print(vogal, end=" ")
    print()
