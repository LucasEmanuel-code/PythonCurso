print("Digite os números para calcular a PA")
p1 = int(input("primeiro termo: "))
r = int(input("razão: "))
pa = p1 + (9 * r)
for c in range(p1, pa, r):
    print(f'{c}', end= "->")