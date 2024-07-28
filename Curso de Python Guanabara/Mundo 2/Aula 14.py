'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1