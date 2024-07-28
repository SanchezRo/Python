n = int(input('Qual numero deseja ver o fatorial? '))
print('{}! = '.format(n), end='')
produto = int (1)
while n > 0:
    print(n, end=' ')
    produto = produto * n
    n -= 1
    if n >= 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
print(produto)