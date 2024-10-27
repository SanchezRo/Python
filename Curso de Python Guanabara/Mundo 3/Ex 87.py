matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceiraColumSoma = 0
maiorSegundaLinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f"Digite um valor para a posição {l}, {c}: "))
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
        if matriz[l][c] == matriz[1][c]:
            if matriz[l][c] > maiorSegundaLinha:
                maiorSegundaLinha = matriz[l][c]

terceiraColumSoma = matriz[0][2] + matriz[1][2] + matriz[2][2]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*10)
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {terceiraColumSoma}')
print(f'O maior valor da segunda linha é: {maiorSegundaLinha}')

