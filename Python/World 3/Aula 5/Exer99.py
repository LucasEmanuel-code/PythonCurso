from time import sleep
num =  [2,9,4,5,7,1]
num2 = [4,7,0]
num3 = [1,2]
num4 = [6]
num5 = [0]
escrito = 'Analizando os valores passados...'
tamanho = '-'*30
def maior(lista):
    print(escrito)
    for valor in lista:
     print(valor, end=' ', flush=True)
     sleep(0.5)
    if lista == [0]:
        print('\nForam infomados 0 valores ao todo.')
    else:
        print(f'\nForam informados {len(lista)} valores ao todo')
        print(f'O maior valor informado foi {max(lista)}')
        sleep(0.5)
    print(tamanho)
maior(num)
maior(num2)
maior(num3)
maior(num4)
maior(num5)