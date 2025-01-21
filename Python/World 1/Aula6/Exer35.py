r1 = float(input('\033[1;33mQuantos cm tem está reta?\033[m '))
r2 = float(input('\033[1;33mE esta reta tem quantos cm?\033[m '))
r3 = float(input('\033[1;33mE esta?\033[m'))
if r2 + r3 >= r1 and r1 + r3 >= r2 and r1 + r2 >= r3:
    print("\033[1;33mPode-se formar um Triangulo\033[m")
else:
    print("\033[1;33mNão pode formar um triangulo, valores errados: {}, {}, {}\033[m".format(r1,r2,r3))
