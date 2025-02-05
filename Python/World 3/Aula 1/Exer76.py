tupla = ('Leite', 10.50, 'Pão', 9.90, 'Molho de churrasco', 18.20,
         'Carne Moida', 25.00, 'Suco de Maracuja', 8.90, 'Nescau', 7.00)

print(35*'=')
print('Lista de Preços')
print(35*'=')
for i in range (0, len(tupla), 2):
    item = tupla[i]
    preco = tupla[i+1]
    print(f'{item.ljust(25)}: R${preco:.2f}')