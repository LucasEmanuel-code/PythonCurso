print("Digite um número")
n = int(input(""))
mult = 1
while True:
    mult += 1
    result = mult * n
    if n < 0:
        print(f"{n} o numero digitado é negativo")
        break
    if mult <= 10:
        print(f"{n} x {mult} = {result}")
print()