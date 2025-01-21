p1 = float(input('\033[7;36;40mO Salário de um funcionário:\033[m '))
p2 = p1 + (p1 * 15 / 100)
cor = { 'd1':'\033[m',
        'd2':'\033[7;35m',
        'd3':'\033[7;36m'}
print('O salário era {}{}{} e teve aumento para {}{}{} de 15% a mais'.format(cor['d2'],p1,cor['d1'],
                                                                    cor['d3'],p2,cor['d1']))