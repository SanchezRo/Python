listagem = ('lapis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 25,
            'transferidor', 4.20,
            'mchila', 120.32)
print('LISTAGEM DE PREÇOS')
print('.'*40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}'.upper(), end='')
    else:
        print(f'R${listagem[pos]:7.2f}')

print('.'*40)