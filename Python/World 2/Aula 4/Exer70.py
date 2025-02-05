print("-"*20)
print("LOJA DO SEU ZÉ")
print("-"*20)

preco_produto = totalcompra = produto_barato = cont = 0
nome_barato = " "

while True:
    nome = str(input("Nome do Produto: "))
    preco = int(input("Preço do Produto: "))
    preco_produto += preco
    cont += 1

    if preco > 1000:
        totalcompra += 1

    if cont == 1 or preco < produto_barato:
        produto_barato = preco
        nome_barato = nome

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()[0]

    if continuar == "n":
        break

print("-"*40)
print(f"Total da compra foi R${preco_produto:.2f}")
print(f"Há {totalcompra} produtos acima de R$1000 reais!")
print(f"O produto mais barato é {nome_barato}")