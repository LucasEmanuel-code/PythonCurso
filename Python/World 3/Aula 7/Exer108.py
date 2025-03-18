from projetos import ex108
print('Digite um preço: ')
num = float(input('R$'))

print(f"Metade: {ex108.moeda(ex108.metade(num))}")
print(f"Dobro: {ex108.moeda(ex108.dobro(num))}")
print(f"Aumento de 10%: {ex108.moeda(ex108.aumento(num))}")
print(f"Diminuição de 13%: {ex108.moeda(ex108.diminui(num))}")