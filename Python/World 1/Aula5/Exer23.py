n = int(input("Digite qualquer número entre 0 a 9999:"))
#n1 = str(int(10000 + n))
#print("{} unidade".format(n1[4]))
#print("{} dezena".format(n1[3]))
#print("{} centena".format(n1[2]))
#print("{} milhar".format(n1[1]))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))