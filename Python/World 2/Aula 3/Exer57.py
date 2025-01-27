Mascu = "M"
Femin = "F"
s = ""

print("Digite seu sexo: ")

while s != Mascu and s != Femin:
    s = input("M para masculino e F para Feminino: ").upper()
    if s == "M":
        print(f"Sexo informado: {s}")
    elif s == "F":
        print(f"Sexo informado: {s}")
    else:
        print("Invalido, digite novamente")