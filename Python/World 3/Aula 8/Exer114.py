import requests
url = "https://www.pudim.com.br/"
try:
    resposta = requests.get(url, timeout= 5)
    if resposta.status_code == 200:
        print('O servidor está disponível.')
    else:
        print('O servidor está indisponível.')
except requests.exceptions.RequestException as erro:
    print(f'Ocorreu um erro ao tentar acessar o servidor')