s = int(0)
cont = int(0)
print('Os numeros mutiplos de 3 entre 1 a 500 são:')
for c in range (1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s = s + c
        cont = cont + 1

print('''
A soma total dos {} valores solicitados é: {}'''.format(cont, s))