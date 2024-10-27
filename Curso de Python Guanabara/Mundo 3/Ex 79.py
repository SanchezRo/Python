listanum = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor Adicionado...')
    else:
        print('Valor duplicado! Não foi possivel adicionar...')
    escolha = input('Deseja Continuar? [S/N]: ')
    if escolha in 'nN':
        break
listanum.sort()
print(f'Valores Adicionados: {listanum}.')