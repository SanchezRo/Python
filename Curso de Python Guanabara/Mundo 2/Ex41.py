from datetime import date

atual = date.today().year
nasc = int(input('Qual a sua Data de Nascimento? '))
idade = atual - nasc
if idade <= 9:
    print('Você compete na categoria MIRIM.')
elif idade <= 14:
    print('Você compete na categoria INFANTIL.')
elif idade <= 19:
    print('Você compete na categoria JUNIOR.')
elif idade <= 20:
    print('Você compete na categoria SENIOR.')
else:
    print('Você compete na categoria MASTER.')