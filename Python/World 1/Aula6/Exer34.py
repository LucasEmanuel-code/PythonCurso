sal = float(input('\033[1;35mQual é seu salário?\033[m '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganahava \033[1;32mR${:.2f}\033[m passa a ganhar \033[1;32mR${:.2f}\033[m agora.'.format(sal,novo))