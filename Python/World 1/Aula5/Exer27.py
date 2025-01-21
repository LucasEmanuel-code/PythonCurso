N1 = str(input("Digite uma seu nome: ")).strip()
name = N1.split()
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {} '.format(name[len(name)-1]))