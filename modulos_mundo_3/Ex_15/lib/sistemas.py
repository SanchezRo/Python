from modulos_mundo_3.Ex_15.lib.arquivos import *
from modulos_mundo_3.Ex_15.lib.interface import *

arq = 'lista_alunos.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # listar contrudo de um arquivo
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Encerrando Operação')
        break
    else:
        print('ERRO! Digite uma opção valida.')