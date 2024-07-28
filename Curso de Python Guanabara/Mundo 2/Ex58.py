from random import randint

print('O computador vai pensar em um Número de 1 a 20.')
n = randint(1, 20)
user = int(input('Em qual Número o computador penssou? '))
cont = int(1)
while user != n:
    print('Você errou!')
    if user < n:
        user = int(input('Tente novamente com um Número maior: '))
    elif user > n:
        user = int(input('Tente novamente com um Número menor: '))
    cont += 1
print('Parabéns, o Número era o {} e você acertou em {} tentativas!'.format(n, cont))
