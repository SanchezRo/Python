while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a/b

    except ValueError:
        print('Tivemos um problema com os tipos de dados digitados!')
    except ZeroDivisionError:
        print('Não é possivel dividir um número por zero!')
    except Exception as erro:
        print(f'Problema encontrado foi {erro.__cause__}!')
    except Exception as erro:
       print(f'Problema encontrado foi {erro.__class__}!')
    except Exception as erro:
        print('Tente Novamente!')


    else:
        print(f'O resultado é {r:.1f}')
        print('Volte Sempre! Muito Obrigado.')
        break