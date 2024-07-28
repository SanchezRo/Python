nome = str()
idade = int()
sexo = str()
mais18 = int()
nOutrosCadastrados = int()
mulheresMenos20 = int()
while True:
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    if idade > 18:
        mais18 += 1
    sexo = str(input('Digite o sexo [M]Masculino, [F] Feminino, [O]Outros: ')).upper().strip()
    if sexo == 'O':
        nOutrosCadastrados += 1
    elif idade < 20 and sexo == 'F':
        mulheresMenos20 +=1
    continua = int(input('Deseja continuar? [1]Sim [2]Não.'))
    if continua == 2:
        break
print(f'Há {mais18} pessoas com mais de 18 anos.')
print(f'Há {nOutrosCadastrados} pessoas que não são Homem ou Mulher.')
print(f'Há {mulheresMenos20} mulheres com menos de 20 anos')
