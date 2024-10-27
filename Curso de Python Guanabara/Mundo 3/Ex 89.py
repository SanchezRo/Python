ficha = list()
aluno = list()
continuar = str('S')
while continuar == 'S':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]


print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*26)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*26)
    opc = int(input('Mostrar notas de qual aluno? (999 Interromper): '))
    if opc == 999:
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
