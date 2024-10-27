num = [2, 5, 9, 1]
num[2] = 3
num.insert(2, 3)
print(num)
'''num[4] = 7'''
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.pop(1)
print(num)
num.remove(3)
print(num)

for c, v in enumerate(num):
    print(f'Na Posição {c} encrontra-se o valor {v}!')

lista = list()
for c in range(0, 8):
    lista.append(int(input('Digite um Valor: ')))
print(f'Os valores inseridos foram: {lista}')

a = [0, 1, 2, 3 ,4]
print(f'lista a: {a}')
b = a
b[2] = 9
''' ^ cria uma ligação, se muda um muda outro'''

c = a[:]
c[2] = 12
''' ^ cria apenas uma copia'''

print(f'lista a: {a}')
print(f'lista a: {b}')
print(f'lista a: {c}')