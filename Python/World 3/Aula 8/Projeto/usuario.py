from arquivo import carregar_usu, salvar_usu

def cad_usu():
    usus = carregar_usu()

    print('\nCADASTRO USUÁRIOS')
    nome = input('Digite seu nome:').strip()
    while True:
        try:
            idade = int(input('Digite sua idade:').strip())
            if idade < 0:
                print('\033[0;31mErro! idade não pode ser negativa nem 0. \033[m')
                continue
            break
        except ValueError:
            print('\033[0;31mErro! Digite uma idade válida. \033[m')
    usus[nome] = {'idade': idade}
    salvar_usu(usus)

def listar_usu():
    usus = carregar_usu()
    cadastrados = 'USUARIOS CADASTRADOS'
    if not usus:
        print('nenhum usuário cadastrado')
        return
    print(cadastrados)
    print('-'*len(cadastrados))
    for nome, dados in usus.items():
        print(f'Nome: {nome} | Idade: {dados['idade']}')
