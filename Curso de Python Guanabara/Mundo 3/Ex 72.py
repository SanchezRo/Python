cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um Número entre 0 e 20: '))
        if 0 <= num <=20:
            break
        print('Tente novamente. ', end='')
    print(f'Voce digitou o número {cont[num]}')
    continua = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    if 'N' in continua:
        break
    else:
        print('-|-'*20)
