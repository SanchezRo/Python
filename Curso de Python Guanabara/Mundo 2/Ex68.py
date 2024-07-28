from random import randint

jogador = int()
computador = int()
vitorias = int()
while True:
    computador = randint(1, 2)
    jogador = int(input('''Escolha: 
[1]IMPAR;
[2]PAR;
Resposta: '''))
    while jogador != 1 and jogador != 2:
        jogador = int(input('''Escolha: 
[1]IMPAR;
[2]PAR;
Resposta: '''))
    print('computador: ',computador)
    print('+++'*20)
    if computador == jogador:
        vitorias += 1
        if jogador == 1:
            print('''O computador também escolheu IMPAR. Você Venceu!''')
        elif jogador == 2:
            print('''O computador também escolheu PAR. Você Venceu!''')
    else:
        if computador == 1:
            print('O computador escolheu IMPAR. Você errou!')
        else:

            print('O computador escolheu PAR. Você errou!')
        print(f'Você Venceu {vitorias} vezes.')
        print('+++'*20)
        break
