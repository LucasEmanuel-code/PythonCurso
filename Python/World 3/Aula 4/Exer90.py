sit = dict()

print('Informe seu Nome e sua Média: ')
sit['nome'] = str(input(''))
sit['media'] = float(input(''))

if sit['media'] > 5:
    print(f'Situação de {sit['nome']}: Aprovado(a)')
else:
    print(f'Situação de {sit['nome']}: Reprovado(a)')