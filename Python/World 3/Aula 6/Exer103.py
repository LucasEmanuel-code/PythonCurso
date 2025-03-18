def ficha(jog='<Desconhecido>', pontos = 0):
    print(f'O jgogador {jog} fez {pontos} pontos na partida ')
n = str(input('Nome do Jogador: ')).strip()
p = str(input('Numero de pontos: '))
if p.isnumeric():
    p = int(p)
else:
    p = 0
if n == '':
    ficha(pontos= p)
else:
    ficha(n, p)



'''nome = str(input("Nome do jogador: ")).strip()
pontos = (input("Pontos na partida: "))
def ficha(nome = '<jogador desconhecido>', pontos=0):
    return f'O jogador {nome} fez {pontos} pontos na partida'
nome = nome if nome else '<jogador desconhecido>'
pontos = pontos if pontos else 0
print(ficha(nome,pontos))'''