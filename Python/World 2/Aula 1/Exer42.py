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
