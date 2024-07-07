peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é ',imc)
if imc < 18.5:
    print('Voce está ABAIXO do peso.')
elif 25 >= imc >= 18.5:
    print('Você está no peso IDEAL.')
elif 25 < imc <= 30:
    print('Você está ACIMA do peso.')
elif 30 < imc <= 40:
    print('Você está sofrendo com OBESIDADE.')
else:
    print('Você está sofrendo com OBESIDADE MORBIDA.')