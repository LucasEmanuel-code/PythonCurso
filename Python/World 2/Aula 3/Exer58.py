import random

cor = {
    'A2': '\033[m',
    'A1': '\033[4;35m',
    'ACERTO': '\033[4;33m',
    'ERRO': '\033[4;34m',
    'TITULO': '\033[4;32m'
}

n2 = random.randint(0, 10)

n1 = -1

while n1 != n2:

    n1 = int(input(f"{cor['TITULO']}O computador pensou em números de 0 a 10, adivinhe o número: {cor['A2']}"))

    if n1 == n2:
        print(f"{cor['ACERTO']}Você acertou! O número era {n2}.{cor['A2']}")
    else:
        print(f"{cor['ERRO']}Você errou! Tente novamente.{cor['A2']}")
