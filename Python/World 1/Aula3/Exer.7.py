f1 = float(input("\033[4;97mDigite a nota do aluno:\033[m"))
f2 = float(input('\033[4;97mDigite a segunda nota do aluno:\033[m'))
f3 = f1 + f2 / 4
cor = {'limpa':'\033[m',
         'azul':'\033[34m'}
print('A média deste aluno é: {}{}{} '.format(cor['azul'],f3,cor['limpa']))