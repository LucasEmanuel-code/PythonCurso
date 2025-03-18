from datetime import date

def voto(n):
    if n < 16:
        return "voce ainda não vota"
    elif 18 <= idade < 65:
        return "seu voto obrigatório"
    else:
        return "seu voto opcional"


ano = int(input('Digite o ano de seu nascimento: '))
anoatual = date.today().year
idade = anoatual - ano

status = voto(idade)
print(f'Com {idade}, {status}')

