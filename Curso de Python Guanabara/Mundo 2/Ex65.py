n = int(0)
media = int(0)
cont = int(0)
escolha = str('')
maior = n
menor = n
total = n
while escolha != 'N':
    if cont == 0:
        n = int(input('Digite um Valor: '))
        maior = n
        menor = n
    else:
        n = int(input('Digite um Valor: '))
    escolha = str(input('Deseja Continuar? [S/N]: ')).upper()
    cont += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    total = total + n
media = total / cont
print('A média entre os {} valores informados é {}, enqunto {} é seu maior valor e {} é seu menor valor, somando um total de {}'.format(cont, media, maior, menor, total))


