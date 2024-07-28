for c in range (1,7):
    print('c')
print('FIM')

print('=-'*10)

for c in range (7, 0,-1):
    print(c)
print('FIM')

print('=-'*10)

n = int(input('Digite um numero: '))
for c in range (0,n+1):
    print(c)
print('FIM')

print('=-'*10)

i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range (i,f,p):
    print(c)
print('FIM')

print('=-'*10)

s = int(0)
for c in range(0,5):
    n = int(input('Digite o {}º valor a ser somado: '.format(c+1)))
    s += n
print('A soma dos valores resulta em: {}'.format(s))