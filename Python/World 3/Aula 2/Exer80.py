valores = list()
while len(valores) < 5:
    num = int(input('Digite um valor: '))
    if num not in valores:
        if not valores or num > valores[-1]:
            valores.append(num)
            print(f'Valor {num} adiconado no final da lista')
        else:
            for i in range(len(valores)):
                if num < valores[i]:
                    valores.insert(i, num)
                    print(f'Valor {num} adicionado na posição {i}')
                    break
    else:
        print('Valor já digitado! Digite outro número.')
if valores:
        print(f'Você digitou os números em ordem crescente: {valores}')