num = int(input('Digite um numero para ver a tabuada: '))
for t in range(1, 11):
    print('{} x {:2} = {}'.format(num, t, num*t))