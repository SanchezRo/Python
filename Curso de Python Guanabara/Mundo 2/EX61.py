termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a progrssão: '))
cont = int(1)
while cont <= 10:
    print(termo, end=' -> ')
    termo = termo + razao
    cont += 1
print('FIM')