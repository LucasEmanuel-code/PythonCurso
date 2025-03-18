try:
    a = int(input(''))
    b = int(input(''))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os dados que vc digitou')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except KeyboardInterrupt:
    print('O usuario prefiriu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'{r}')
finally:
    print('Volte sempre! Thank you')