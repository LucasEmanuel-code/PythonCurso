sal= float(input('\033[4;34mQual é o saláario do funconário?\033[4;43m'))
new = sal + (sal + 15 / 100)
print('\033[4;30;107mO funcionario ganhava {:.2f} e agora ganha R${:.2f} com o disconto de 15%\033[m'.format(sal, new))