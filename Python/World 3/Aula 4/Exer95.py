from time import sleep
dadosjogadores = []

while True:
    dadosusuario = dict()
    dadosusuario['nome'] = str(input("Nome do jogador da NBA: "))
    dadosusuario['pontos'] = []

    print()
    quant = int(input(f"Quantas partidas {dadosusuario['nome']} jogou? "))
    print()

    for c in range(quant):
        pontos = int(input(f"Quantos pontos {dadosusuario['nome']} fez na partida {c + 1}? "))
        dadosusuario["pontos"].append(pontos)

    dadosusuario['total'] = sum(dadosusuario["pontos"])
    quant_real = len(dadosusuario['pontos'])

    dadosjogadores.append(dadosusuario)

    continuar_jogador = input("Deseja registrar outro jogador? [S/N]: ").strip().lower()
    if continuar_jogador == 'n':
        break

print('-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Pontos":>8}')
print('-' * 30)
for i, jogador in enumerate(dadosjogadores):
    total_pontos = sum(jogador['pontos'])
    print(f'{i + 1:<4}{jogador["nome"]:<10}{total_pontos:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))

    if opc == 999:
        print('Finalizando...')
        sleep(1)
        print('Programa finalizado com sucesso!')
        break

    if 1 <= opc <= len(dadosjogadores):
        jogador_escolhido = dadosjogadores[opc - 1]  # Subtrai 1 para acessar corretamente a lista
        print(f'Pontos de {jogador_escolhido["nome"]}: {jogador_escolhido["pontos"]}')
    else:
        print('Opção inválida, tente novamente.')
