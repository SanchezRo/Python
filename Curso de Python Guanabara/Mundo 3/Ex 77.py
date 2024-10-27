palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR')
for v in palavras:
    print(f'\nNa Palavra {v} Temos: ', end=' ')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
