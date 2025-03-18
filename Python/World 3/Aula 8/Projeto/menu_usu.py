from usuario import cad_usu, listar_usu
from time import sleep

def menu():
    sistema = '\nSISTEMA DE CADASTRO'
    while True:
        print(sistema)
        print('-'*len(sistema))
        print('1. Cadastro de Usuário')
        print('2. Lista de Usuários')
        print('3. Sair')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cad_usu()
        elif opcao == '2':
            listar_usu()
        elif opcao == '3':
            print('Saindo...')
            sleep(0.5)
            print('Finalizado com Sucesso!')
            break
        else:
            print('\033[0;31mOpção inválida! Tente novamente.\033[m')