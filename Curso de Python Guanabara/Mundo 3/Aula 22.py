from modulos_mundo_3 import numeros #caso esteja apenas dentro do primeiro package
from modulos_mundo_3.numeros import funcoes

# Importação do package da aula de funcoes



num = int(input('Digite um valor: '))
fat = funcoes.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {funcoes.dobro(num)}')