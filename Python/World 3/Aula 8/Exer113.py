def leiaInt(msg):
    while True:
        try:
           n = int(input(msg))
           return n
        except ValueError:
            print('\033[0;31mErro digite um numero inteiro valido\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuario prefire não informar o numero\033[m')
def leiafloat(msg):
    while True:
        try:
            r = float(input(msg))
            return r
        except ValueError:
            print('\033[0;31mErro digite um numero real valido\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuario prefere não informar o real\033[m')
n = leiaInt('Digite um numero: ')
r = leiafloat('Digite um número real: ')
print(f'O foi digitado o inteiro {n} e o real {r}')