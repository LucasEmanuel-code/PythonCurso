print('Escreva 3 frases')
uso = str(input(''))
uso2 = str(input(''))
uso3 = str(input(''))

tamanho = len(uso)

def escreva(escrever):

    print('-'*tamanho)
    print(escrever)
    print('-'*tamanho)

escreva(uso)
escreva(uso2)
escreva(uso3)
