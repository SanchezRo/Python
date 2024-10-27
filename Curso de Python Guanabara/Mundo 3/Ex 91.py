from operator import itemgetter
from random import randint
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
rank = list()
print('Valores sorteados:')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rank)
for i, v in enumerate(rank):
        print(f'{i+1}º lugar: {v[0]}  com {v[1]}')