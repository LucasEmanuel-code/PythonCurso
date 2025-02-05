from random import randint

vitorias = 0

while True:
    print("Digite um número: ")
    n = int(input(""))

    if n < 0:
        print("Escolha inválida! tente novamente")
        break

    computer = randint(0, 10)

    soma = n + computer

    print("Par ou Impar?")
    escolha = input("").strip().lower()

    result = "par" if soma % 2 == 0 else "impar"

    print(f"Voce jogou {n}, o computador {computer}. Total deu {soma}, {result.upper()}")

    if escolha == result:
        vitorias +=1
        print("Voce acertou")
    else:
        print("Voce errou")
        print(f"Total de vitórias: {vitorias}")
        break