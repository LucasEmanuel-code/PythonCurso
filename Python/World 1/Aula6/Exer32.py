from datetime import date
ano = int(input("\033[7;97;40mDiga-me um ano qualquer:\033[m "))
cor = {'D2':'\033[m',
       'D1':'\033[7;30;107m'}
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[7;97;40mEste ano\033[m {}{}{} \033[7;97;40mé bissexto\033[m".format(cor['D1'],
                                                                                ano, cor['D2']))
else:
    print("\033[7;97;40 mEste ano\033[m {}{}{} \033[7;97;40mnao é bissexto\033[m".format(cor['D1'],
                                                                                  ano,cor['D2']))