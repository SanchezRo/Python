def notas(*n, sit=False):
    """
    => Função para analizar notas e situação de alunos.
    :param n: uma ou mais notas de alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com varias informações sobre a situação da turma.
    """
    r=dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


situacao = bool
sn = str(input('Deseja visualizar a Situação? [S/N] ')).strip().upper()
if sn == 'S':
    situacao = True

resp = notas(10, 8, 5, sit = situacao)
print(resp)