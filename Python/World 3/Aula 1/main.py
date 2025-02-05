#Tuplas
lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
#tuplas sao imutaveis

# lanche[1] = 'Refrigerante' está errado X

for cont in range(0, len(lanche)): #uso do range
    print(f'comerei {lanche[cont]} na posição {cont}')

print(len(lanche))
for pos, comida in enumerate(lanche): #variavel composta
    print(f"comerei {comida} na posição {pos}")
print("Comi muito")

#com o numero negativo "-1" o print retorna o elemento ao contriario
# -1 retorna = pudim

#com o numero de "1:3" leva do 2 elemento até o penultimo elemento
# 1:3 retorna = suco e pizza

#com o numero "0:" leva do primeiro elemento até o ultimo elemento
# 0: retorna = hambuger, suco, pizza, pudim

#com o numero ":2" leva do primeiro elemento até o penultimo elemento
# :2 retorna = hambuguer, suco

#com o numero "-2:" leva elemento contrario até o ultimo elemento
# -2: retorna: pizza, pudim