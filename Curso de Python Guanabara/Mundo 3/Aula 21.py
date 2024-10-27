from mimetypes import inited
from time import sleep


def contador(i, f, p):
    print('Iniciando Contador...')
    c = i
    while c <= f:
        sleep(0.5)
        print(f'{c}', end='...')
        print()
        sleep(0.5)
        c += p
    print('Fim!')


print('Contador')
print('-=' *35)
inicio = int(input('Digite onde inicia o Contador: '))
fim = int(input('Digite onde finaliza o Contador: '))
passo = int(input('Digite quantos passos da o Contador: '))

contador(inicio, fim, passo)

print('-='*35)
print('-='*35)
print()

#  GLOBAL
def funcao(b):
    global a
    a = 8
    b += 4

#   RETURN
def somar(a, b, c):
    s = a+b+c
    return s

r1 = somar(3, 5, 7)
r2 = somar(2, 8, 0)
print(f'meus calculos com return são: {r1} e {r2}')

print()

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número'))
f1 = fatorial(n)
print(f'o fatorial de {n} é igual a {f1}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número'))
if par(num):
    print('É par!')
else:
    print('Não é Par')