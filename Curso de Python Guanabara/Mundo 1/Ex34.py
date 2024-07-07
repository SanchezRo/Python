salario = float(input("Qual o seu salario? R$"))
if salario <= 1250.00:
    almento = 0.15
    salarioAlment = salario + salario * almento
else:
    almento = 0.10
    salarioAlment = salario + salario * almento
print("O salário de R${:.2f} subiu para R${:.2f}, recebendo um almento de {:.0f}%.".format(salario, salarioAlment, almento*100))