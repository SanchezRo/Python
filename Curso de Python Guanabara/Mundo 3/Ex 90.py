aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
aluno['situacao'] = str()

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

'''for k, v in aluno.items():
        print(f' - {k} é igual a {v}')
'''

print('-='*32)
print('NOME', ' '*30, 'MÉDIA', ' '*10, 'SITUAÇÃO')
print(f'{aluno['nome']:^34}', f'{aluno["media"]:^7}', ' '*9, f'{aluno['situacao']:^9}')