pessoas = []

while True:
    dados = dict()

    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))

    dados['sexo'] = input("M ou F: ").strip().lower()
    while dados['sexo'] not in ("m", "f"):
        dados['sexo'] = input("M ou F: ").strip().lower()

    pessoas.append(dados)

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()
    print()

    if continuar == "n":
        break

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
if len(pessoas) > 0:
        soma_idades = sum(dados['idade'] for dados in pessoas)
        media_idades = soma_idades / len(pessoas)
        print(f'A média das idades é {media_idades:.2f}')

        mulher = [dados for dados in pessoas if dados['sexo'] == 'f']
        if mulher:
            print("Nomes das mulheres cadastradas:")
            for mulheres in mulher:
                print(f"{mulheres['nome']}")

        acima = [dados for dados in pessoas if dados['idade'] > media_idades]

        print('Pessoas acima da média: ')
        print()

        for pessoas in acima:
            print(f'Nome: {pessoas['nome']} \n'
                  f'Idade: {pessoas['idade']} \n'
                  f'Sexo: {pessoas['sexo']}'.lower())
            print()
else:
    print('Nenhuma pessoa cadastrada')