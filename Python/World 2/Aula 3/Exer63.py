print("Digite um número: ")
n = int(input(""))

n1 = 0
n2 = 1

cont = 3

print("Sequencia de Fibonacci: ")
print(f"{n1} -> {n2}", end="")
while cont <= n:
    n3 = n1 + n2
    print(f" -> {n3}", end="")
    n1 = n2
    n2 = n3
    cont += 1