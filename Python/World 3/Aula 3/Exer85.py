parimpar = [[], []]
print('Digite 7 numeros: ')

for c in range(7):
    num = int(input())
    if num % 2 == 0:
        parimpar[0].append(num)
    else:
        parimpar[1].append(num)

parimpar[0].sort()
parimpar[1].sort()

print(f'Pares:', parimpar[0])
print(f'Impar:', parimpar[1])

