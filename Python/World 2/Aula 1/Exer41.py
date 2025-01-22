from datetime import date
print("Digite sua data de Nascimento: ")
anos = int(input(""))

ano2 = date.today().year

ano3 = ano2 - anos

print("Sua categoria na natação é: ")
if ano3 <= 9:
    print(f"Mirim, idade: {ano3}")
elif ano3 <= 14:
    print(f"Infantil, idade: {ano3}")
elif ano3 <= 19:
    print(f"Junior, idade: {ano3}")
elif ano3 <= 20:
    print(f"Senior, idade: {ano3}")
else:
    print(f"Master, idade: {ano3}")
42
r1 = float(input('Quantos cm tem está reta? '))
r2 = float(input('E esta reta tem quantos cm? '))
r3 = float(input('E esta? '))
if r2 + r3 >= r1 and r1 + r3 >= r2 and r1 + r2 >= r3:
    if r1 == r2 == r3:
        print("pode se formar um triangulo equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("pdoe se formar um triangulo isoceles")
    else:
        print("O triangulo é escaleno")
else:
    print("Pode se formar um triangulo")
