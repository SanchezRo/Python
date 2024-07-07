from time import sleep

print('Bom Dia!')
velocidade =float(input('Qual a velocidade do carro em Km/h? '))
print('-=-' * 20)
print('PROCESSANDO...')
sleep(2)
print(' ')
if velocidade <= 80:
    print('A velocidade de {}Km/h não ultrapassou o limite de 80Km/h.'.format(velocidade))
    print('Vecê está dentro do Limite de Velocidade!')
    print('Tenha um bom dia!')
    print('Dirija com segurança.')
else:
    print('A velocidade de {}Km/h ultrapassou o limite de 80Km/h.'.format(velocidade))
    print('Você foi Multado em R$7,00 por cada Km/h acima do limite!')
    multa = (velocidade-80) * 7
    print('Sua Multa é de R${:.2f}!'.format(multa))
