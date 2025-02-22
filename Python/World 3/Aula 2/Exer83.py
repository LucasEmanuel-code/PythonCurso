e = str(input('Digite uma expressão matematica: '))
valor = []
valida = True
for c in e:
    if c == '(':
        valor.append('(')
    elif c ==')':
        if len(valor) > 0:
            valor.pop()
        else:
            valor.append(')')
            break
if len(valor) == 0:
    print('Expressao valida!')
else:
    print('Expressao invalida')