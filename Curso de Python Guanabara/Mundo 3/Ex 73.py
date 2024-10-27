times = ('a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't')

print('Lista de Times: ')
for t in times:
    print(t)
print('+'*30)

print('Os 5 Primeiros Colocados são: ')
for t in range(0, 5):
    print(times[t])
print('+'*50)

print('Os 4 Ultimos Colocados são:')
for t in range(19, 15, -1):
    print(times[t])
print('+'*50)

print(f'Times em Ordem Alfabética: {sorted(times)}')
print('+'*50)

print(f'O "H" está na {times.index("h")+1}ª Posição')
