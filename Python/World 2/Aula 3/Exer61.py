print("Digite os números para calcular a PA")
p1 = int(input("primeiro termo: "))
r = int(input("razão: "))

cont = 1
term = p1

while cont <= 10:
    term += r
    cont += 1
    print(f'{term}', end= " -> ")