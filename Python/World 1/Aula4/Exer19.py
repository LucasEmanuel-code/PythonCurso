from random import choice
A1 = input("\033[32mNome do pimeiro Aluno(a):\033[m ")
A2 = input("\033[33mNome do segundo Aluno(a):\033[m ")
A3 = input("\033[34mNome do terceiro Aluno(a):\033[m ")
A4 = input("\033[32mNome do quarto Aluno(a):\033[m ")
lista = [A1, A2, A3, A4]
#escolhida = random.choice(lista)
Es = choice(lista)
cor= {'N1':'\033[m',
      'N2':'\033[31m'}
print("A(o) Aluna(o) Sorteado(a) foi {}{}{}".format(cor['N2'],Es,cor['N1']))
