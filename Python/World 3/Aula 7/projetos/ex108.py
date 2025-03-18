def metade(n, formatado=False):
    result = n // 2
    if formatado:
        return moeda(result)
    else:
        return result

def aumento(n, formatado=False):
    n2 = n * 0.10
    result = n + n2
    if formatado:
        return moeda(result)
    else:
        return result

def dobro(n, formatado=False):
    result = n * 2
    if formatado:
        return moeda(result)
    else:
        return result

def diminui(n, formatado= False):
    n2 = n * 0.13
    result = n - n2
    if formatado:
        return moeda(result)
    else:
        return result

def moeda(n):
        valor = n
        formatado = "R${:,.2f}".format(valor).replace(',', 'X').replace('.', ',').replace('X', '.')
        return formatado

