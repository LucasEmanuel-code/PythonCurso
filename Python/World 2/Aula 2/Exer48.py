impar = 1
soma = 0
for c in range(1, 501, 2):
    soma += impar
    impar += 2
print(soma)
