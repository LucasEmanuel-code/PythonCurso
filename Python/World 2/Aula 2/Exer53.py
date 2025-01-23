print("Digite uma palavra ou frase para verificar se é um palíndromo: ")
palavra = input("").strip().lower()

palavra = palavra.replace(" ","")

palavra2 = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra2 += palavra[i]

if palavra == palavra2:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
