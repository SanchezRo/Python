pessoas = list()
pessoa = dict()
cadastro = True
c = 0
somaIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    pessoa['sexo'] = str(input('Sexo [M/F/O]: ').upper())

    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']

    pessoas.append(pessoa.copy())
    t = input('Quer continuar? [S/N] ').upper()
    c += 1
    if t in 'N':
        break

print('-='*30)
print(f'Cadastro no Sistema: {len(pessoas)} Pessoas')
print(f'Idade Média: {somaIdade/c} Anos')
print('-='*30)
print('Mulheres Cadastradas:')
for s in pessoas:
    if s['sexo'] in 'F':
        print(f'{s['nome']} ', end='')
        print()
print('-='*30)
print('Pessoas Acima da Média de Idade:')
for p in pessoas:
    if p['idade'] > somaIdade/c:
        print(f'{p["nome"]} ', end='')
        print()