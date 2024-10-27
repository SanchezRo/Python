num = (int(input('Digite um numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite outro numero: ')))
print(f'Voce digitou: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu ma {num.index(3)+1}ª posição')
print('Os valores pares digitados foram: ')
for n in num:
    if n%2 == 0:
        print(n)