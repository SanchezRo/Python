import math

catOp = float(input('Digite o valor do Cateto Oposto: '))
catAd = float(input('Digite o valor do Cateto Adjacente: '))

hipotenusa = math.hypot(catOp, catAd)
print('A hipotenusa é: ', hipotenusa)

