print("Digite o nome, idade e sexo de 4 pessoas: ")

maior_idade = 0
soma_idade = 0
nome_velho = ""
nome_homem = False
qnt_mulher_20 = 0

for c in range(1, 5):
    nome = input("Nome: ")
    sexo = input("M ou F: ").strip().lower()
    idade = int(input("Idade: "))

    soma_idade += idade

    if sexo == "m" and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
        nome_homem = True

    if sexo == "f" and idade < 20:
        qnt_mulher_20 += 1

media = soma_idade /4

print(f"A idade média do grupo é {media} ")
if nome_homem:
    print(f"O nome do homem mais vélho do grupo é {nome_velho} com {maior_idade} anos")
else:
    print("Não há homens no grupo")
print(f"A quantidade de mulheres com menos de 20 anos é {qnt_mulher_20}")