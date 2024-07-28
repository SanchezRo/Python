sexo = input('Digite o sexo [M] ou [F]: ').upper().strip()
while sexo != 'M' and sexo != 'F':
    print('''Informação Invalida!
Por Favor, Tente Novamente!''')
    sexo = input('Digite o sexo [M] ou [F]: ').upper().strip()
print('Informação registrada')