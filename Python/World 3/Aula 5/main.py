'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} e {b} é {s}')


soma(b=4, a=5)
soma(7, 2)'''

'''def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('fim')

    tam = len(num)
    print(f'Recebi {num} e são ao todo {tam} numeros')
contador(5, 7, 3, 1, 4)
contador(2,0)
contador(8, 9, 3, 5)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)