nomeProd = str()
preco = float()
total = float()
maisBarato = str()
precoMaisBarato = float(0)
maisDeMil = int(0)

while True:
    nomeProd = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$'))

    if precoMaisBarato == 0:
        precoMaisBarato = preco
    if precoMaisBarato > preco:
        precoMaisBarato = preco
        maisBarato = nomeProd
    if preco > 1000:
        maisDeMil += 1
    total += preco

    continua = int(input('Deseja continuar? [1]Sim [2]Não: '))
    if continua == 2:
        break
print(f'Foram grastos R${total} no total.')
print(f'{maisDeMil} produtos custam mais de R$1000,00.')
print(f'O produto mais barato é o(a) {maisBarato}.')