time = list()
jogador = dict()
partidas = dict()
while True:
    jogador['nome'] = input('Nome: ')
    jogador['partidas_jogadas'] = int(input('Partidas jogadas: '))
    if jogador['partidas_jogadas'] > 0:
        jogador['gols'] = int(0)
        partidas.clear()
        for i in range(jogador['partidas_jogadas']):
            partidas[1+i] = int(input(f'Gols na partida {1+i}: '))
            jogador['gols'] += partidas[1+i]

    time.append(jogador.copy())
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break

print('=-'*35)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-'*35)
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Tente novamente!')
    else:
        print(f' -- Levantamendo do jogador {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'Na partida {i+1} fez {g} gols.')


