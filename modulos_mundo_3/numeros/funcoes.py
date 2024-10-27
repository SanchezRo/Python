def fatorial(n):
    f =1
    for c in range(1, n+1):
        f += c
    return f


def dobro(n):
    return n*2


def triplo(n):
    return n*3


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Por Favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de Dados Interrompida!')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Por Favor, digite um número válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de Dados Interrompida!')
            return 0
        else:
            return n
