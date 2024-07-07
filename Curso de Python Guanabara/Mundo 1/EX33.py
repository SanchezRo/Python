n1 = int(input('Digite o 1º Número: '))
n2 = int(input('Digite o 2º Número: '))
n3 = int(input('Digite o 3º Número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor número é: ', menor)
print('O maior número é: ', maior)