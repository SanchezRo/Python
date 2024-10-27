lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    escolha = input('Deseja continuar? [S/N]: ')
    if escolha in 'Nn':
        break

print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Segue valores em ordem decrescente: {lista}')
if 5 in lista:
   print('O Valor 5 faz parte da lista.')
else:
   print('O Valor 5 não foi encontrado na lista.')