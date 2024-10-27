import funcoes


num = int(input('Digite um valor: '))
fat = funcoes.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {funcoes.dobro(num)}')

''''''''''''''''''''''''''''''''''''

from funcoes import *


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}')