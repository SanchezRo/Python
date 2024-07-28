
somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ºPESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


mediaIdade = somaIdade / 4
print('')
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomeVelho, maiorIdadeHomem))
print('Ao todo são {} Mulheres com menos 20 anos.'.format(totmulher20))
