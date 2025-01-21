from math import hypot
ca = int(input("\033[33mcateto adjecente:\033[m "))
co = int(input("\033[34mcateto oposto:\033[m "))
hi = hypot(ca, co)
print("\033[31mO comprimeito do cateto oposto vale {} e do cateto adjecente vale {} e da hipotenusa vale {}\033[m".format(co, ca, hi))