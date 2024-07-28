n = int(input('Quantos termos da sequencia de fibonacci deseja ver: '))
cont = int(0)
t1 = int(0)
t2 = int(1)
t3 = int(0)
print('{} - {}'.format(t1, t2), end=' - ')
while cont < n:
    cont += 1
    t3 = t1 + t2
    print(t3, end = ' - ')
    t1 = t2
    t2 = t3
print('Fim')