n1 = int(input('\033[33mDigite um número:\033[m '))
n2 = int(input('\033[32mDigite outro numemro:\033[m '))
n3 = int(input('\033[34mDigite outro número:\033[m '))
maior = n1
menor = n1
cor = {'D1':'\033[33m',
       'D2':'\033[32m',
       'D3':'\033[m'}
if maior< n2:
    maior = n2

if maior < n3:
    maior = n3

if menor > n2:
    menor = n2

if menor > n3:
    menor = n3

print('\033[35mMaior:\033[m {}{}{}'.format(cor['D1'],maior,cor['D3']))
print('\033[35mMenor:\033[m {}{}{}'.format(cor['D2'],menor,cor['D3']))
