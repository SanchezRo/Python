from random import randint

tupla = (randint(1, 99), randint(1, 99), randint(1, 99),
         randint(1, 99), randint(1, 99))
print('Os Valores Sorteados Foram:')
for t in tupla:
    print(f'{t}')
print(f'O Maior número é: {max(tupla)}')
print(f'O Menor é número é: {min(tupla)}')









'''from random import randint

num = int()
tupla = (int())
maior = int()
menor = int()
for t in range(0 , 6):
    num = randint(1, 99)
    tupla = (num)
    if t == 0:
        maior = num
        menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
print(tupla)
print(f'O Maior número é: {maior}')
print(f'O Menor é número é: {menor}')'''
