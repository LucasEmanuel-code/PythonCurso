s1 = int(input('\033[7;35;40mDigite apenas um número:\033[m'))
s2 = s1 * 2
s3 = s1 * 3
s4 = s1 **(1/2)
print("O seu número é \033[4;36m{}\033[m, e o dobro é \033[4;36m{}\033[m,o triplo é \033[4;32m{}\033[m e a raíz quadrada é \033[4;34m{}\033[m".format(s1, s2, s3, s4))