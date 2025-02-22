alunos = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])

    continuar = input('\nQuer continuar? (S/N)').strip().lower()
    if continuar == 'n':
        break

print('-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'* 35)
    opc = int(input('Mostarar notas de qual aluno? (999 para o programa): '))
    if opc == 999:
        print('Finzalizado...')
        break
    if opc <= len(alunos) -1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('Volte sempre')
