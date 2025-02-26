pessoas = []

while True:
    dados = dict()

    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))

    dados['sexo'] = input("M ou F: ").strip().lower()
    while dados['sexo'] not in ("m", "f"):
        dados['sexo'] = input("M ou F: ").strip().lower()

    pessoas.append(dados)

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
    print()

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
if len(pessoas) > 0:
        soma_idades = sum(dados['idade'] for dados in pessoas)
        media_idades = soma_idades / len(pessoas)
        print(f'A média das idades é {media_idades:.2f}')

        print('As mulheres cadastradas foram: ', end='')
        for p in pessoas:
            if p['sexo'] in 'Ff':
                print(f'{p["nome"]}', end=' ')
        print()
        print()

        print('Lista das pessoas que estão acima da média: ')
        for p in pessoas:
            if p['idade'] >= media_idades:
                print('   ', end='')
                for k, v in p.items():
                    print(f'{k} = {v}; ', end='')
                print()
        print('<< Encerrado >>')
else:
    print('Nenhuma pessoa cadastrada')