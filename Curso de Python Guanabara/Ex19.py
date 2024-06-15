import random

aluno1 = str(input('Digite o nome do Aluno:'))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do Aluno: '))
aluno4 = str(input('Digite o nome do Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(' O aluno escolhido foi: ', escolhido)
