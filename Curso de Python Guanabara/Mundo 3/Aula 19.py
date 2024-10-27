pessoas = dict()
cadPessoas = list()
for c in range(0, 3):
    pessoas['id'] = c+1
    pessoas['nomes'] = input('Digite seu nome: ')
    pessoas['idade'] = int(input('Digite sua idade: '))
    pessoas['sexo'] = input('Digite seu sexo: ')
    cadPessoas.append(pessoas.copy())
for e in cadPessoas:
    for v in e.values():
        print(v, end=' ')
    print()