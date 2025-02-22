cadastros = []
tot = 0
maior_peso = menor_peso = 0
pessoas_maior_peso = []
pessoas_menor_peso = []

print('Informe seu nome e peso: ')
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    cadastros.append((nome, peso))
    tot += 1

    if tot == 1:
        maior_peso = menor_peso = peso
        pessoas_maior_peso = [nome]
        pessoas_menor_peso = [nome]
    else:
        if peso > maior_peso:
            maior_peso = peso
            pessoas_maior_peso = [nome]
        elif peso == maior_peso:
            pessoas_maior_peso.append(nome)

        if peso < menor_peso:
            menor_peso = peso
            pessoas_menor_peso = [nome]
        elif peso == menor_peso:
            pessoas_menor_peso.append(nome)

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()
    if continuar == "n":
        break

print(f'\nA quantidade de pessoas cadastradas é {tot}')

print(f'O maior peso é {maior_peso}Kg. Peso de: ', end="")
for pessoa in pessoas_maior_peso:
    print(f'{pessoa}', end=" ")

print(f'\nO menor peso é {menor_peso}Kg. Peso de: ', end="")
for pessoa in pessoas_menor_peso:
    print(f'{pessoa}', end=" ")