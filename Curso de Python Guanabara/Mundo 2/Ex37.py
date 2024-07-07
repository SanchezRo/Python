num = int(input('Qual o numero inteiro que deseja converter? '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para Binario.
[ 2 ] Converter para Octal.
[ 3 ] Converter para Hexadecimal.''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} convertido para Binario é igual {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual {}.'.format(num, hex(num)[2:]))
else:
    print('A Opção inserida é inválida.')