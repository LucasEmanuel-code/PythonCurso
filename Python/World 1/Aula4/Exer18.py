from math import sin, cos, tan, radians

A = float(input("\033[36mDigite o angulo da circunferencia(ou seja, entre 0º e 360º):\033[m "))
S = sin(radians(A))
C = cos(radians(A))
T = tan(radians(A))

print("\033[32mO angulo de {} tem o seno de {: .2f}.\033[m".format(A, S))
print("\033[33mO angulo de {} tem o seno de {: .2f}.\033[m".format(A, C))
print("\033[34mO angulo de {} tem o seno de {: .2f}.\033[m".format(A, T))
