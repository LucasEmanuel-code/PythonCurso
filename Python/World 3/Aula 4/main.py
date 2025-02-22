estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


'''brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[1]['uf'])'''


'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''



#print(f'O {pessoas['nome']} tem {pessoas['idade']} anos') resultado: O Gustavo tem 22 anos
#print(pessoas.keys()) resultado: dict_keys(['nome', 'sexo', 'idade'])
#print(pessoas.values()) resultado: dict_values(['Gustavo', 'M', 22])
#print(pessoas.items()) resultado: dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])