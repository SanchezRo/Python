from tkinter import PanedWindow
from modulos_mundo_3.Ex_15.lib.interface import cabecalho


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do Arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO na leitura do Arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())