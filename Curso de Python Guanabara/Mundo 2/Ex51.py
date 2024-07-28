primeiroTermo = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
termo10 = primeiroTermo + (10-1) * razao
for c in range (primeiroTermo, termo10 + razao, razao):
    print('{}'.format(primeiroTermo), end=' - ')
    primeiroTermo = primeiroTermo + razao
print('FIM!')