n1 = int(input('\033[7;97mDIgite um valor: '))
n2 = int(input('\033[7;97mDIgite outro valor: \033[m'))
s = n1 + n2
# print('A soma entre:', n1 ,'e', n2, 'vale:', s)
print('A soma entre \033[31m{}\033[m e \033[97m{}\033[m vale \033[34m{}\033[m'.format(n1,n2,s))