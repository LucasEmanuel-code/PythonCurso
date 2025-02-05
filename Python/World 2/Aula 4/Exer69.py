print("CADASTRO DE PESSOAS")

soma_i = 0
total_homens = 0
maior_18 = 0
mulher_20 = 0
homem = False

while True:
    i = int(input("Idade: "))

    sexo = input("M ou F: ").strip().lower()
    while sexo not in ("m", "f"):
        sexo = input("M ou F: ").strip().lower()

    soma_i += i

    if sexo == "m":
        total_homens += 1
        homem = True
    elif sexo == "f" and i < 20:
        mulher_20 += 1

    if i > 18:
        maior_18 += 1

    continuar = input("Deseja continuar? [S/N]: ").strip().lower()

    if continuar == "n":
        break

# Exibir resultados após sair do loop
print("\nRESULTADOS:")
print(f"Total de pessoas cadastradas com mais de 18: {maior_18}")
print(f"Quantidade de homens cadastrados: {total_homens}" if homem else "Não há homens cadastrados")
print(f"Quantidade de mulheres com menos de 20 anos: {mulher_20}")
