dadosusuario = dict()

dadosusuario['nome'] = str(input("Nome do jogador da NBA: "))
partidas = list()
print()

quant = int(input(f"Quantas partidas {dadosusuario['nome']} jogou? "))
print()

for c in range(quant):
    partidas.append(int(input(f"Quantos pontos na partida {c + 1}? ")))

dadosusuario['pontos'] = partidas[:]
dadosusuario['total'] = sum(partidas)

print()
print(dadosusuario)

print()
print(f'O campo nome tem valor {dadosusuario['nome']}')
print(f'O campo pontos tem valor {partidas}')
print(f'O campo total tem o valor {dadosusuario['total']}')

print()
print(f'O jogador {dadosusuario['nome']} jogou {quant} partidas')
for c in range(quant):
    print(f'Na partida {c + 1}, fez {dadosusuario['pontos'][c]} pontos')
print(f'Foi um total de {dadosusuario['total']} pontos')