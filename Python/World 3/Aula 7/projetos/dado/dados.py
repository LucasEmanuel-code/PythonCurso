def leiadinheiro(msg):
    """

    :param msg:
    :return:
    """
    while True:
        n = input(msg).strip().replace(',', '.')
        if n.replace('.','', 1).isdigit():
            n = float(n)
            if n >= 0:
                return n

        print(f'Erro! {n} não é um número válido')