def fatorial(n, show):
    """
    -> Calcula fatorial de um numero
    :param n: O numero a ser calculado
    :param show: Mostrar a conta (opcional)
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    while n > 0:
        f = f * n
        if show == True:
            print(n, end=' ')
            if n == 1:
                print('=', end=' ')
                break
            print('x', end=' ')
        n = n-1
    print(f)
fatorial(5, show=True)
help(fatorial)