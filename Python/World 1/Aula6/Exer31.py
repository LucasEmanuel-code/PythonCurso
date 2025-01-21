dis = float(input('\033[34mQual a distancia da viagem?\033[m '))
passagem1 = dis * 0.50
passagem2 = dis * 0.45
if dis <= 200:
    print("Você percorreu menos de 200km/h entao ficou  R$ \033[7;34m{}\033[m a passagem".format(passagem1))
else:
    print("Você percorreu mais de 200km/h entao ficou  R$ \033[7;35;107m{}\033[m a passagem".format(passagem2))