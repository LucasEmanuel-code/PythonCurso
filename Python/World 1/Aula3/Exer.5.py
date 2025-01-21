s1 = int(input("\033[4;97mDigite apenas um número: \033[m"))
b1 = s1 + 1
b2 = s1 - 1
print("O sucesor deste número \033[31m{}\033[m é \033[34m{}\033[m, e seu antecessor é \033[35m{}\033[m".format(s1, b1, b2))