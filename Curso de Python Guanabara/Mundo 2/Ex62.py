termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a progrssão: '))
cont = int(1)
qnt = int(10)
total = int(10)
while qnt != 0:
    while cont <= total:
        print(termo, end=' -> ')
        termo = termo + razao
        cont += 1
    print('FIM')
    qnt = int(input('Quantos termos mais gostaria de ver? '))
    total = total + qnt
print('Até a Proxima!')