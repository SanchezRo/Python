from random import randint
from time import sleep

computador = randint(0,5) #sorteia um numero
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #recebe o numero do jogador
print(' ')
print('PROCESSANDO...')
sleep(2)
print(' ')
if jogador == computador:
    print('Parabéns, você acertou!!!')
else:
    print('Ah! Que Peninha!!!')
    print('Eu pensei no numero {}'.format(computador))
    print('Poxa, não foi dessa vez. Mas continue tentando!')