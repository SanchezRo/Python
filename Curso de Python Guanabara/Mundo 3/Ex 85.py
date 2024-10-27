n=[[], []]
impar = []
par = []

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
n=par,impar
par.sort()
impar.sort()
print('-='*10)
print(f'Você Digitou: {n}')
print(f'Os Números Pares são: {par}')
print(f'Os Números Impares são: {impar}')