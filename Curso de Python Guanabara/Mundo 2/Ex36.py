salario = float(input('Qual o seu salario? '))
precoCasa = float(input('Qual o valor da casa? '))
tempoPag = int(input('Em quantos anos vai ser financiada? '))
meses = tempoPag * 12
parcela = precoCasa / meses
if parcela > (0.3 * salario):
    print('Você não pode fazer o empréstimo para a compra desta casa!')
else:
    print(('Parabéns!!! Seu em préstimo foi aprovado no valor de R${:.2f}, para ser pago em {} vezes de R${:.2f}.'.format(precoCasa, meses, parcela)))
print('Volte Sempre!!!')
