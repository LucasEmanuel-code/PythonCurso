nome=input('Qual é o nome da sua cidade? ')
nome.strip()
print('Essa cidade começa com "Santos"? ')
print(nome[0:6].lower()=='santos')