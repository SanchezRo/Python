dados = dict()
dados['nome'] = input('Nome: ')
dados['partidas_jogadas'] = int(input('Partidas jogadas: '))
if dados['partidas_jogadas'] > 0:
    dados['gols'] = int(0)
    partidas = dict()
    for i in range(dados['partidas_jogadas']):
        partidas[1+i] = int(input(f'Gols na partida {1+i}: '))
        dados['gols'] += partidas[1+i]

print('=='*20)
for k, v in dados.items():
    print(f'{k}:   -- {v} --')

print('=='*20)
for k, v in partidas.items():
    print(f'Na partida {k} foram {v} gols.')