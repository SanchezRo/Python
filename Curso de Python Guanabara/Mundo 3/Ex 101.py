def voto(int):
    from datetime import date
    idade = date.today().year - int
    if idade < 16:
        return(f'Com {idade} anos: Voto Negado!')
    elif 16 <= idade < 18 or idade >= 65:
        return(f'Com {idade} anos: Voto Opcional!')
    else:
        return(f'Com {idade} anos: Voto Obrigatório!')


anoNasc = int(input('Digite o ano de nascimento: '))
print(voto(anoNasc))