lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('Digite um Valor: ')))
    escolha = input('Deseja Continuar? [S/N]: ')
    if escolha in 'nN':
        break

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])

print(f"Você digitou os valores: {lista}")
print(f'Os Numeros Pares são: {par}')
print(f'Os Numeros Impares são: {impar}')