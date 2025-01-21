import random
n1 = int(input('\033[4;32mO computador pensou em números de 0 a 5 advinhe o numero:\033[m '))
n2 = random.randint(0,5)
cor = {'A2':'\033[m',
       'A1':'\033[4;35m'}
if n1 == n2:
   print("\033[4;33mVocê acertou\033[m")
else:
   print('\033[4;34mVocê errou, o número era {}{}{}\033[m'.format(cor['A1'],n2,cor['A2']))

#from random import randint
#from time import sleep
#computador = randint(0,5) # Faz o computador "PENSAR"
#print("-=-" * 20)
#print("Vou pensar em um número entre 0 e 5, Tente advivinhar...")
#print("-=-" * 20)
#jogador = int(input("Em que número eu pensei?")) # joggador tenta adivinhar
#print("Processando...")
#sleep(3)
#if jogador == computador:
#    print("PARABÉN! Você venceu")
#else:
#    print("GANHEI! Eu pensei no número {}".format(computador))