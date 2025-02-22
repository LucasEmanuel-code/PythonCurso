dadosusuario = dict()

dadosusuario['nome'] = str(input("Nome do jogador da NBA: "))
dadosusuario['pontos'] = []
print()

quant = int(input(f"Quantas partidas {dadosusuario['nome']} jogou? "))
print()

for c in range(quant):
    pontos = int(input(f"Quantos pontos {dadosusuario['nome']} fez na partida {c + 1}? "))
    dadosusuario['pontos'].append(pontos)

total_pontos = sum(dadosusuario['pontos'])
print()
print(f'O campo nome tem valor {dadosusuario['nome']}')
print(f'O campo pontos tem valor {dadosusuario['pontos']}')
print(f'O campo total tem o valor {total_pontos}')

print()
print(f'O jogador {dadosusuario['nome']} jogou {quant} partidas')
for c in range(quant):
    print(f'Na partida {c + 1}, fez {dadosusuario['pontos'][c]} pontos')