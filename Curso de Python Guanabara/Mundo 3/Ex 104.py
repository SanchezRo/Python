def leiaInt():
    r = input('Digite um Número Inteiro: ')
    if r.isnumeric():
        print(f'Você Digitou o Nº{r}!')
    else:
        while r != r.isnumeric():
            print('ERRO! Digite um Valor Válido.')
            print('-='*30)
            r = input('Digite um Número Inteiro: ')
            if r.isnumeric():
                print(f'Você Digitou o Número {r}!')
                break


leiaInt()