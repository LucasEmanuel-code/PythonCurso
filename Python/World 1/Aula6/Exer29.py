velo = float(input('\033[35mEm quantos km o carro ultrapassou?\033[m'))
cor = {'A2':'\033[m',
       'A1':'\033[32m'}
if velo > 80:
    print('\033[33mVocê foi multado, o limete é 80km/h\033[m')
    multa = (velo - 80) * 7
    print("\033[35mSua multa é de\033[m {}{}{} \033[35mreais\033[m".format(cor['A1'],multa, cor['A2']))
else:
    print("\033[36mVocê nao foi multado\033[m")