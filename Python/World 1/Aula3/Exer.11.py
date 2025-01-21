money = float(input("\033[7;33;42mDigite o preço do produto:\033[m "))
desconto = money - (money * 5 / 100)
print('a camisa vale RS\033[32m{}\033[m, e com desonto de 5% vale RS\033[33m{}\033[m'.format(money, desconto))