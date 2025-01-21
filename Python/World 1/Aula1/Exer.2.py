nome = input ('\033[7;97mDigite seu nome: \033[m')
cor = {'jao':'\033[7;97m',
       'joa':'\033[m'}
print ('É um prazser em te conhecer {}{}{}!'.format(cor['jao'],nome,cor['joa']))