num1 = int(input('Digite o primeiro numero a ser comparado: '))
num2 = int(input('Digite o segundo numero a ser comparado: '))
if num1 > num2:
    print('O primeiro número, {}, é maior que o segundo número, {}.'.format(num1,num2))
elif num2 > num1:
    print('O segundo número, {}, é maior que o primeiro número, {}.'.format(num2,num1))
else:
    print('Os valores digitados são iguais.')