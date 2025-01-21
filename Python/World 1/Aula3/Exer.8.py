s1 = int(input("\033[7;34mDigite um número:\033[m "))
s2 = s1 * 100
s3 = s1 * 1000
cor = {'dois':'\033[m',
       'tres':'\033[34m',
       'quatro':'\033[31m',
       'cinco':'\033[32m'}
print('Seu número em metros {}{}{}, \n seu número em cm {}{}{} \n e seu número em mm {}{}{}'.format(cor['tres'],s1,cor['dois'],
                                                                                                cor['quatro'],s2,cor['dois'],
                                                                                                cor['cinco'],s3,cor['dois']))