print("Quais foram as 2 notas deste aluno?")
n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))

n3 = (n1 + n2)/2

if n3 >= 7.0:
    print(f"Parabéns, sua nota foi {n3} você foi aprovado!")
elif 5.0 <= n3 < 7.0:
    print(f"Você está de recuperação, sua nota foi {n3}.")
else:
    print(f"Infelizmente, você foi reprovado, sua nota foi {n3}.")
