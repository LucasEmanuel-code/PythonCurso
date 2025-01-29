n = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont += n
print(f"A soma vale {cont}")

#cont = 1
#while cont <= 10:
#    print(cont, "->", end="")
#    cont += 1
#print("ACABOU"

#Apenas a estrutura "While True" faz com que fique
# infinitamente contando os numeros
