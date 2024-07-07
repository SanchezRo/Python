import math

ang = int(input('Digite um angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O angulo de {} possui: ')
print('Seno: {:.2f}'.format(sen))
print('cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))