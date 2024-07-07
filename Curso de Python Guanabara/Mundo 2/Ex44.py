preco = float(input('Digite o valor do produto: '))
pag = int(input('''Escolha a fomra de pagamento:
[1] À Vista no Dinheiro;
[2] À Vista no Cartão;
[3] Até 2x no Cartão;
[4] 3x ou mais no Cartão;
Digite o Número da Escolha: '''))
if pag == 1:
    preco = preco - preco*0.1
    print('O valor total da compra ficou: R${:.2f}'.format(preco))
elif pag == 2:
    preco = preco - preco*0.05
    print('O valor total da compra ficou: R${:.2f}'.format(preco))
elif pag == 3:
    parcelas = int(input('Será dividido em quantas parcelas: [1] ou [2]: '))
    if parcelas == 1:
        print('O valor total da compra ficou: {}x de R${:.2f}'.format(parcelas, preco))
    elif parcelas == 2:
        preco = preco / parcelas
        print('O valor total da compra ficou: {}x de R${:.2f}'.format(parcelas, preco))
    else:
        print('Valor Invalido!')
elif pag == 4:
    preco = preco + preco*0.2
    parcelas = int(input('Será dividido em quantas parcelas: '))
    preco = preco / parcelas
    print('O valor total da compra ficou: {}x de R${:.2f}'.format(parcelas, preco))
else:
    print('Escolha Invalida!')
