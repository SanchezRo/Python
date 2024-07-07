n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
media = (n1 + n2)/2
if media < 5.0:
    print('''Sua média é {:.2f}.
A média mínima necessária para aprovação é 6.9.
Você foi reprovado!'''.format(media))
elif media >= 5.0 and media < 7:
    print('''Sua média é {:.2f}.
A média mínima necessária para aprovação é 6.9.
Você precisará fazer a recuperação!'''.format(media))
else:
    print('''Sua média é {:.2f}.
A média mínima necessária para aprovação é 6.9.
Você foi aprovado!'''.format(media))