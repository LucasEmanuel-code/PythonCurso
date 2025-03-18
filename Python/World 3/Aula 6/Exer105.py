def notas(*n, sit):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da Turma
    """
    media = sum(n) / len(n)
    total = len(n)
    maior = max(n)
    menor = min(n)
    dado = {'total':total, 'maior': maior, 'menor': menor, 'media': media, 'situação': sit}
    if sit:
        if media >= 5:
            dado['situação'] = 'Aprovado'
        elif n == 5:
            dado['situação'] = 'Recuperação'
        else:
            dado['situação'] = 'Reprovado'
    else:
        del dado['situação']
    return dado
resp = notas(5.5,9.5,10,6.5, sit=True)
print(resp)
help(notas)