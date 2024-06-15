salario = float(input('Qual o Salario do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O Salario de {:.2f} com aumento de 15% totaliza: R${:.2f }'.format(salario, aumento))