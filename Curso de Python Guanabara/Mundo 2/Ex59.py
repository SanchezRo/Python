n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
result = int(0)
escolha = int(0)
while escolha != 5:
    escolha = int(input('''Escolha uma das opções abaixo:
    [1] Somar;
    [2] Multiplicar;
    [3] Achar o Maior;
    [4] Novos Valores;
    [5] Sair do Programa;
    Escolha: '''))
    if escolha == 1:
        result = n1 + n2
        print('A Soma entre {} e {} é igual a: {}'.format(n1, n2, result))
    elif escolha == 2:
        result = n1 * n2
        print('A Multiplicação entre {} e {} é igual a: {}'.format(n1, n2, result))
    elif escolha == 3:
        if n1 > n2:
            print('O 1º Valor, {}, é maior que o 2º Valor, {}.'.format(n1, n2))
        else:
            print('O 2º Valor, {}, é maior que o 1º Valor, {}.'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor'))

print('Volte Sempre!')