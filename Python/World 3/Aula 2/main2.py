valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite o valor: ')))

for c, v in enumerate(valores):
    print(f'Na posiçaõ {c} encontrei o valor {v}!')
print("Cheguei ao final")

"""a = [2,3,4,7]
b = a[:] #Cópia da lista, muda somente a lista b
b[2] = 8
print(f'A: {a}')
print(f'B: {b}')"""