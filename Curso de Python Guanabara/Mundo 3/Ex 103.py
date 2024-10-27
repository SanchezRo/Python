def ficha(jog = '<desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gols no campeonato.')

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)