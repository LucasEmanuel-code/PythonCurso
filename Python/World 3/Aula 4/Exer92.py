from datetime import date
pessoa = dict()
pessoa2 = list()

pessoa['nome'] = str(input('Nome: '))
pessoa['ano'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - pessoa['ano']
pessoa['ctps'] = int(input('Informe seu ctps(0 caso não tenha): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação:'))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - pessoa['ano']) + 35
else:
    pessoa['contratacao'] = None
    pessoa['salario'] = None
    pessoa['aposentadoria'] = None

pessoa2.append(pessoa.copy())

for p in pessoa2:
    print('\nCadastro: ')
    for k, v in p.items():
        print(f'{k.capitalize()}: {v}')
