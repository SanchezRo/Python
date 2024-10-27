def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


show = bool()
num = int(input('Qual o número que deseja ver o fatorail? '))
sN = str(input('Deseja mostrar o processo na tela? S/N: ')).upper().strip()
if sN in 'Ss':
    show = True
elif sN in 'Nn':
    show = False

print(fatorial(num, show))