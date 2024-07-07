idade = int(input('Qual a sua idade? '))
if idade < 18:
    tempo = 18 - idade
    print('Ainda falta(m) {} ano(s) para você poder se alistar.'.format(tempo))
elif idade == 18:
    print('Parabéns, você já pode se alistar. Corra para não perder o prazo!')
else:
    confimação = (input('''Você realizou fez o alistamento quando tinha 18 anos?
Digite [S] para SIM ou [N] para NÃO. 
'''))
    if confimação == 's' or confimação == 'S':
        print('Parabéns, você esta com seu alistamento em dia.')
    elif confimação == 'n' or confimação == 'N':
        tempo = idade - 18
        print('Você perdeu o prazo de alistamento. Você deveria ter se alista a {} ano(s).'.format(tempo))
    else:
        print('''Resposta Invalida.
        Tente Novamente!''')