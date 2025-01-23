from datetime import date
print("Digite o ano de nascimento de sete pessoas: ")

ano3 = 0
ano = date.today().year
for c in range(1, 8):
    pessoas = int(input(""))
    ano2 = ano - pessoas
    if ano2 >= 18:
        ano3 += 1

print(f"{ano3} ja são maiores de idade")