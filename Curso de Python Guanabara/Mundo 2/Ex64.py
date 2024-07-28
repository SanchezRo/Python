n = int(0)
total = int(0)
cont = int(0)
while n != 999:
    total = total + n
    cont += 1
    n = int(input('Digite um Número [999 para parar]: '))
cont -= 1
print('Foram informados {} valores, somando {} no total.'.format(cont, total))