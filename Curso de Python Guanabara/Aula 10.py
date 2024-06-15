nome = str(input('qual o seu nome: '))
if nome == 'Rodrigo':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print('Bom Dia, {}!'.format(nome))

print('----------------------------------')

n1 = float(input('Qual a nota da primeira Prova?'))
n2 = float(input('Qual a nota da segunda Prova?'))
media = (n1+n2)/2
print('sua média é: ', media)
if media >= 7:
    print("Parabéns! Você foi aprovado.")
else:
    print("Você foi reprovado, estude mais para passar na próxima")

