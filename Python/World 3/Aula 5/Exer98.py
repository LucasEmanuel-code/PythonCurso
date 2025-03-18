from time import sleep
def contador():
    print('Contagem de 1 até 10 de 1 em 1')
    for num in range(1, 11):
        print(num, end=' ', flush=True)
        sleep(0.5)
    print()
    print('\nContagem de 10 até 0 de 2 em 2')
    for num in range(10, -1, -2):
        print(num, end=' ')
        sleep(0.5)
    print()
    print('\nAgora é a sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p == 0:
        if i <= f:
            for num in range(i, f + 1):
                print(num, end=' ', flush=True)
                sleep(0.5)
        else:
            for num in range(i, f - 1, -1):
                print(num, end=' ', flush=True)
                sleep(0.5)
    elif p > 0:
        for num in range(i, f + 1, p):
            print(num, end=' ', flush=True)
            sleep(0.5)
    elif p < 0:
        for num in range(i, f - 1, p):
            print(num, end=' ', flush=True)
            sleep(0.5)
    else:
        print("Passo não pode ser zero!")
    print()
    print("\nContagem personalizada concluída!")
contador()
