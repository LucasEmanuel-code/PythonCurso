import random
from time import sleep

print("Vamos jogar jokenpô")
print("Escolha papel, tesoura ou pedra: \n"
      "Papel\n"
      "Tesoura\n"
      "Pedra")
p1 = (input(""))

sleep(1)
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Pô")


opcoes = ["Papel", "Tesoura", "Pedra"]

pc = random.choice(opcoes)
print(f"O computador escolheu: {pc}")

if p1 == pc:
     print("Empate")
elif p1 == "Pedra" and pc == "Tesoura":
    print("Você ganhou")
elif p1 == "Papel" and pc == "Pedra":
    print("Você ganhou")
elif p1 == "Tesoura" and pc == "Papel":
    print("Você")
else:
    print("Você perdeu!")