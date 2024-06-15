preco = float(input('Qual o preço do produto? '))
desconto = float(input('Qual a porcentagem do desconto a ser aplicado? '))
total = preco - (desconto * preco / 100)
print('O preço do produto,R${}, com o desconto de {}% é: {:.2f}'.format(preco, desconto, total))