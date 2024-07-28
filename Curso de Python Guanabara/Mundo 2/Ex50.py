soma = int(0)
c = int(0)
for c in range(1, 7):
    num = int(input('Digite o {}º Número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        c = c + 1
print('A soma dos numeros pares dentre os {} informados resulta em: {}'.format(c, soma))