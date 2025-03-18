from projetos.moeda import resumo
from projetos.dado import leiadinheiro

print('Digite um preço: ')
num = leiadinheiro('R$ ')
resumo(num, True)