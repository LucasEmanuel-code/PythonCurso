n1 = int(input("Digite um número: "))

print("Escolha uma base de conversão\n"
      "[1] binário\n"
      "[2] octal\n"
      "[3] hexodecimal\n")

n2 = int(input("Escolha um número acima: "))

if n2 == 1:
    print(bin(n1))
elif n2 == 2:
    print(oct(n1))
elif n2 == 3:
    print(hex(n1))
else:
    print("escolha um número valido")
