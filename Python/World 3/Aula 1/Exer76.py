tupla = ('Leite', 10.50, 'Pão', 9.90, 'Molho de churrasco', 18.20,
         'Carne Moida', 25.00, 'Suco de Maracuja', 8.90, 'Nescau', 7.00)

print(40*'-')
print(f'{"LISTA DE PREÇOS":^40}')
print(40*'-')
for i in range (0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30} R${tupla[i+1]:.2f}')
print('-' * 40)