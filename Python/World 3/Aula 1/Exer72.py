numero = ('zero', 'um', 'dois',
          'tres', 'quatro', 'cinco',
          'seis', 'sete', 'oito',
          'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete',
          'dezoito', 'dezenove', 'vinte')

while True:
    print("Digite um numero:")
    n = int(input(""))

    if 0 <= n <= 20:
        break
print(f"Numero digitado: {numero[n]}")