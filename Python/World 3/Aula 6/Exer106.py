c = ('\033[m', '\033[0;30;41m', '\033[0;30;45m', '\033[0;30;44m')

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[1], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-'*tam)
    print(f'   {msg}')
    print('-' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('Sistema de ajuda pyhelp',2)
    comando = str(input('Função ou Bilioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo',1 )



'''sys = 'SISTEMA DE AJUDA PyHELP'
def sistem(msg):
    if msg == 'Fim':
        print('Encerrando...')
        return None
    else:
        return msg
tamanho = len(sys)
print('-'*tamanho)
print(sys)
print('-'*tamanho)
entrada = input('Digite uma Função ou Biblioteca > ')
f = sistem(entrada)
if f and f != 'Fim':
    help(f)'''