print("Digite os números para calcular a PA")
p1 = int(input("primeiro termo: "))
r = int(input("razão: "))

cont = 1
term = p1
opcao = 10

while opcao != 0:
    for c in range(opcao):
        term += r
        cont += 1
        print(f'{term}', end= " -> ")
    print("PAUSA")

    opcao = int(input("Quantos termos vc quer mostrar?"))

print("Finalizado")