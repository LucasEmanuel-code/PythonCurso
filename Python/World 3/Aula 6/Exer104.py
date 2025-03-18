def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro digite um numero inteiro valido\033[m')
        if ok:
            break
    return valor
n = leiaInt('Digite um numero inteiro: ')
print(f'{n}')



'''def leiaInt(msg):
    while True:
        entrada = input(msg)
        valido = True
        i = 0
        while i < len(entrada):
            if '0' <= entrada[i] <= '9':
                i += 1
            else:
                valido = False
                break
        if valido:
            result = 0
            i = 0
            while i < len(entrada):
                result = result * 10 + (ord(entrada[i])-48)
                i += 1
            return result
        else:
            print('\033[0;31mErro digite um número inteiro!\033[m')
n = leiaInt('Digite um numero inteiro: ')
print(n)'''