valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite o valor: ')))
print(f'voce digitou os numeros: {valores}')

maior = max(valores)
menor = min(valores)

print(f'O menor valor digitado foi {menor} na(s) posição(ões)', end='')
for i, c in enumerate(valores):
    if menor == valores[i]:
        print(i, end='...')

print(f'\nO maior valor digitado foi {maior} na(s) posição(ões)', end='')
for d, b in enumerate(valores):
    if maior == valores[d]:
        print(d, end='...')

