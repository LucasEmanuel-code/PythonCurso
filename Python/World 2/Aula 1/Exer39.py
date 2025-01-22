from datetime import date

ano = int(input("Em que ano voce nasceu? "))

data = date.today().year

ano2 = data - ano

ano3 = 18 - ano2

if ano2 < 18:
    print(f"ainda vai se alistar, falta {ano3} anos para poder se alistar")
elif ano2 == 18:
    print("já é hora de se alistar")
else:
    print("já passou do tempo de se alistar")
