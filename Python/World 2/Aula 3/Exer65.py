soma = contador =  0
maior = 0
menor = 0
entrada = 1
cont = "sim"

while cont != "nao" and "não":
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1

    if entrada == 1:
        maior = numero
        menor = numero
        entrada = 0
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    print("Deseja continuar? Sim ou Não?")
    cont = input("").strip().lower()

if contador > 0:
    media = soma / contador
    print(f"A média dos números é: {media} \n"
          f"A soma dos números é: {soma} \n"
          f"O maior número lido foi: {maior}, e o menor foi {menor}")
else:
    print("Nenhum número válido foi digitado.")
