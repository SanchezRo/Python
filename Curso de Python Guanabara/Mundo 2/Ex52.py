n = int(input('Digite um número: '))
cont = int(0)
for c in range (1, 11):
    if n % c == 0:
        cont = cont +1
    print('{} / {} = {:.2f}'.format(n, c, n/c))
if cont != 2:
    print('''O numero {}, foi divizivel por números além de 1 e por ele mesmo.
Logo, {} não é um número primo.'''.format(n, n))
else:
    print('''O numero {}, foi divizivel apenas pelo número 1 e por ele mesmo.
Logo, {} é um número primo.'''.format(n, n))
