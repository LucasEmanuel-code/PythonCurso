def leiadinheiro(msg):
    while True:
        n = input(msg).strip().replace(',', '.')
        if n.replace('.','', 1).isdigit():
            n = float(n)
            if n >= 0:
                return n
        print(f'\033[0;31mErro! \'{n}\' não é um número válido\033[m')