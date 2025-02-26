from datetime import date
pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['ctps'] = int(input('Informe seu ctps(0 caso não tenha): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação:'))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - nasc) + 35
print('-='*30)

print('\nCadastro: ')
for k, v in pessoa.items():
    print(f' - {k.capitalize()}: {v}')
