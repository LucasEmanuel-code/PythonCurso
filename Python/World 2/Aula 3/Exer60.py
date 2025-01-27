print("Digite um número: ")
n1 = int(input(""))
c = n1
fat = 1
while c > 1:
    fat *= c
    c -= 1
    print(f"{c}", end="")
    print(f" x " if c > 1 else " = ", end="")
print(f"{fat}")