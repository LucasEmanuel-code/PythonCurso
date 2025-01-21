N1 = str(input("Digite uma frase: ")).upper().strip()
print('A letra "A" aparece {} no nome'.format(N1.count('A')))
print('A letra "A" aparece na {} posição da frase'.format(N1.find("A")+1))
print('A letra "A" aparece na {} posição da frase'.format(N1.rfind("A")+1))

