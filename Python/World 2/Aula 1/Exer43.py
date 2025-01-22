print("Descreva sua altura e peso: ")
peso = float(input(""))
altura = float(input(""))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso Ideal")
elif 25 < imc < 30:
    print("Sobre Peso")
elif 30 < imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
