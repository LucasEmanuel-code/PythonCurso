num = [2, 5, 9, 1]

num[2] = 3 # Adiciona o 3 na 2 posição da lista e remove o 9

num.append(7) # Adiciona o 7 na lista

num.sort(reverse=True) # "num.sort" deixa em ordem crescente, com "reverse=True" deixa ao contrario

num.insert(2,2) # Adiciona mais um numero na lista em tal posição sem remover o numero

#num.pop(2) #Remove o numero de tal posição da lista
if 4 in num:
    num.remove(4) #Remove o numero da primeira posição
else:
    print('Nao achei o numero 4')

print(num)
print(f'essa lista tem {len(num)} numeros')