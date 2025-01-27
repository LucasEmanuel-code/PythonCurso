from time import sleep

print("Digite 2 números: ")
n1 = int(input(""))
n2 = int(input(""))

opcao = 0

while opcao != 5:
    print("Escolha apenas 1 no Menu: \n"
      "[1]somar\n"
      "[2]multiplicar\n"
      "[3]maior\n"
      "[4]novos números\n"
      "[5]sair do programa")

    opcao = int(input(""))

    if opcao == 1:
        soma = n1 + n2
        print(f"a soma deu: {soma}")
    elif opcao == 2:
        mult = n1 * n2
        print(f"a multiplicação deu: {mult}")
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f"o maior numero é: {maior}")
    elif opcao == 4:
        print("Digite 2 números: ")
        n1 = int(input(""))
        n2 = int(input(""))
    elif opcao == 5:
        print("Saindo do programa...")
        sleep(2)
    else:
        print("Invalido, digite novamente!")

