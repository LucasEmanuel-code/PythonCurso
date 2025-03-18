#def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela
#    :param i: inicio da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    Função criada por Gusta Guanara do canal CursoEmVideo
#    """
#   c = i
#    while c <= f:
#        print(f'{c}', end=' ')
#        c+= p
#    print('Fim!')
# help(contador)

#def somar(a = 0, b = 0, c = 0):
#    """
#    -> Faz a soma de três valores e mostra o resultado na tela
#    :param a: o primeiro valor
#    :param b: o segundo valor
#    :param c: o terceiro valor
#    Função criada por Gusta Guarana do canal Curso Video
#    """
#    s = a + b + c
#    print(f'A soma vale {s}')
#somar(3,2,5)
#somar(8,4)
#somar(0)
#somar(3,3,5)
#somar(b = 4, c=2)

#def teste(b):
#    global a
#    a = 8
#    b+= 4
#    c = 2
#    print(f'{a}')
#    print(f'{b}')
#    print(f'{c}')
#a= 5
#teste(a)
#print(f'fora {a}')

#def funcao():
   # n1 = 4
   # print(f'N1 dentro vale {n1}')

#n1 = 2
#funcao()
#print(f'N1 fora vale {n1}')

def somar (a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')