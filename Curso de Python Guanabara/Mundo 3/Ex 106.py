
def manualPython(com):
    titulo(f'Acessando o manual do comando {com}')
    help(com)


def titulo(msg,cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        manualPython(comando)
titulo('ATÉ LOGO!')