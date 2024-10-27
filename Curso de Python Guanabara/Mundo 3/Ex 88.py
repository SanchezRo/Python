from random import randint

nJogos = int(input('Quantos jogos quer jogar? '))
jogo = list()
listaDeJogos = list()
n = 0

while n <= nJogos:
   cont = 0
   while True:
        nSelec = randint(1, 60)
        if nSelec not in jogo:
            jogo.append(nSelec)
            cont += 1
        if cont >= 6:
            break
   jogo.sort()
   listaDeJogos.append(jogo[:])
   jogo.clear()
   n += 1

for i, l in enumerate(listaDeJogos):
    print(f'Jogo {i+1}: {l}')