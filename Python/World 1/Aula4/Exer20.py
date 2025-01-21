import random
a1 = str(input("\033[32mNome do primeiro Aluno(a):\033[m "))
a2 = str(input("\033[33mNome do segundo Aluno(a):\033[m "))
a3 = str(input("\033[34mNome do terceiro Aluno(a):\033[m "))
a4 = str(input("\033[35mNome do quarto Aluno(a):\033[m "))
grup = [a1, a2, a3, a4]
random.shuffle(grup)
print('\033[36m{}\033[m'.format(grup))